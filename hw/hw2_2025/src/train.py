import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import argparse
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import torch
import torchvision

from models.lenet import LeNet
from utils import pre_process


def plot_loss_curve(
        loss_values,
        title="Training Loss Curve",
        xlabel="Epoch",
        ylabel="Average Loss",
        color="blue",
        linestyle="-",
        linewidth=1,
        marker="o",
        save_path=None,
        dpi=300,
):
    epochs=np.arange(1,len(loss_values)+1)  #epoch编号

    plt.figure(figsize=(10,6))  #创建画布

    plt.plot(epochs, loss_values,
             color=color,linestyle=linestyle,linewidth=linewidth,marker=marker) #绘制图线

    plt.title(title,fontsize=14)
    plt.xlabel(xlabel,fontsize=12)  #标题和坐标轴名
    plt.ylabel(ylabel,fontsize=12)

    plt.grid(True,linestyle='--',alpha=0.7)  #网格线
    plt.tight_layout()  #调整布局

    if save_path:
        plt.savefig(save_path,dpi=dpi)  #如果要保存的话

    plt.show()  #显示图像


def get_data_loader(batch_size):
    # MNIST dataset
    train_dataset = torchvision.datasets.MNIST(root='data/',
                                               train=True,
                                               transform=pre_process.data_augment_transform(),
                                               download=True)

    test_dataset = torchvision.datasets.MNIST(root='data/',
                                              train=False,
                                              transform=pre_process.normal_transform())

    # Data loader
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                               batch_size=batch_size,
                                               shuffle=True)

    test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                              batch_size=batch_size,
                                              shuffle=False)


    return train_loader, test_loader


def evaluate(model, test_loader, device, save_error_dir='error_samples', max_errors=5):
    model.eval()
    os.makedirs(save_error_dir, exist_ok=True)
    error_samples = []  # 存储错误样例信息

    with torch.no_grad():
        correct = 0
        total = 0

        for images, labels in test_loader:

            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)

            # 计算总精度
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            # 筛选错误样例
            errors = (predicted != labels)
            if errors.any() and len(error_samples) < max_errors:
                error_imgs = images[errors].cpu()
                error_labels = labels[errors].cpu().numpy()
                error_preds = predicted[errors].cpu().numpy()

                # 保存错误样例（逐个检查，避免超过max_errors）
                for i in range(len(error_imgs)):
                    if len(error_samples) >= max_errors:  # 检查是否已达到最大数量
                        break

                    # 图像格式转换
                    img = error_imgs[i].squeeze().numpy()
                    img = (img * 255).astype(np.uint8)
                    pil_img = Image.fromarray(img)

                    # 保存图像（使用实际保存的样本索引命名）
                    save_path = os.path.join(save_error_dir,
                                             f'error_{len(error_samples) + 1}_true_{error_labels[i]}_pred_{error_preds[i]}.png')
                    pil_img.save(save_path)

                    # 记录错误信息
                    error_samples.append({
                        'image_path': save_path,
                        'true_label': error_labels[i],
                        'pred_label': error_preds[i]
                    })

    # 打印精度
    print('Test Accuracy of the model is: {:.2f} %'.format(100 * correct / total))
    return error_samples

def save_model(model, save_path='lenet.onnx'):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    model.eval()
    dummy_input = torch.randn(1, 1, 28, 28).to(device)
    torch.onnx.export(model, dummy_input, save_path)

# def save_model(model, save_path='lenet.pth'):
#     ckpt_dict = {
#         'state_dict': model.state_dict()
#     }
#     torch.save(ckpt_dict, save_path)


def train(epochs, batch_size, learning_rate, num_classes):

    # fetch data
    train_loader, test_loader = get_data_loader(batch_size)

    # Loss and optimizer
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    model = LeNet(num_classes).to(device)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)  #更换为SGD（当然可以调冲量啥的，默认就行）

    loss_values = [] #用来记录loss

    # start train
    total_step = len(train_loader)
    for epoch in range(epochs):
        epoch_total_loss = 0.0  # 记录总loss

        for i, (images, labels) in enumerate(train_loader):

            
            # get image and label
            images = images.to(device)
            labels = labels.to(device)

            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)
            
            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            epoch_total_loss += loss.item()  #计算epoch的总loss

            if (i + 1) % 100 == 0:
                print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'
                      .format(epoch + 1, epochs, i + 1, total_step, loss.item()))

        epoch_avg_loss = epoch_total_loss / total_step  # 计算平均loss
        loss_values.append(epoch_avg_loss)

        # evaluate after epoch train
        error_samples =evaluate(model, test_loader, device)



    # 打印前5个错误样例信息（用于分析）
    print("\n前5个错误样例信息：")
    for i, sample in enumerate(error_samples, 1):
        print(
            f"样例{i}：真实标签={sample['true_label']}，预测标签={sample['pred_label']}，图像路径={sample['image_path']}")

    # save the trained model
    save_model(model, save_path='lenet.onnx')
    plot_loss_curve(loss_values)
    return model


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--batch-size', type=int, default=256)
    parser.add_argument('--lr', type=float, default=0.001)
    parser.add_argument('--num_classes', type=int, default=10)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    train(args.epochs, args.batch_size, args.lr, args.num_classes)


