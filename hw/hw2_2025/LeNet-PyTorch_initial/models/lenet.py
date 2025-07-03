import torch


class LeNet(torch.nn.Module):
    def __init__(self, num_classes=10):
        super(LeNet, self).__init__()

        # TODO: Add extra convolutional layer here
        ### CODE START

        self.layer1 = torch.nn.Sequential(
            torch.nn.Conv2d(1, 16, kernel_size=5, stride=1, padding=2),
            torch.nn.BatchNorm2d(16),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = torch.nn.Sequential(
            torch.nn.Conv2d(16, 32, kernel_size=5, stride=1, padding=2),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2))

        self.layer3 = torch.nn.Sequential(
            torch.nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),  # 新增的卷积层3——更温和地提取特征
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2))

        ### CODE END

        self.fc = torch.nn.Linear(3 * 3 * 64, num_classes)   #3 = (7 + 2 × 1 - 3) / (1 + 1)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        if self.layer3 is not None:
            out = self.layer3(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        return out