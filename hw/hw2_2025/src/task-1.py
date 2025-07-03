import torch
import torchvision

from utils import visualizer

if __name__ == '__main__':

    train_dataset = torchvision.datasets.MNIST(root='data/',
                                               train=True,
                                               transform=torchvision.transforms.ToTensor(),
                                               download=True)


    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                               batch_size=128,
                                               shuffle=True)

    for i, (images, labels) in enumerate(train_loader):
        # visualize images
        visualizer.demo_display_specific_digit_combination(images, labels)
