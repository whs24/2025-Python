import torchvision


def normal_transform():
    normal = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
    ])
    return normal

def data_augment_transform():
    data_augment = torchvision.transforms.Compose([
        torchvision.transforms.RandomCrop(28, padding=4),  # 随机剪裁（MNIST的原始尺寸是28×28）
        torchvision.transforms.RandomHorizontalFlip(p=0.5),  # 随机水平翻转（概率设为了0.5）
        torchvision.transforms.RandomRotation(degrees=15),  # 随机旋转（±15度）
        torchvision.transforms.ToTensor(),
    ])
    return data_augment
