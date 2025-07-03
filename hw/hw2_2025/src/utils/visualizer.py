import cv2
import torch


def display_image(img, target_size=None):
    if target_size:  #调整图像大小
        ratio = target_size / max(img.shape[0], img.shape[1])
        interp = cv2.INTER_AREA
        img = cv2.resize(img, (int(img.shape[1] * ratio), int(img.shape[0] * ratio)), interpolation=interp)
    cv2.imshow("", img)  #显示图像
    cv2.waitKey(0)


def demo_display_single_image(images, labels):
    image_to_display = images[0]
    image_to_display = image_to_display.numpy()  #转换成numpy格式
    image_to_display = image_to_display.transpose(1, 2, 0)  #调整路径
    display_image(image_to_display, target_size=240)
    label = labels[0]
    cv2.imwrite(f"{label.item}.jpg", image_to_display)  #保存图片


def demo_display_specific_digit_combination(images, labels):
    assert images.shape[0] == labels.shape[0]

    # this is an example for retrieve digits image
    digit_image_dict = {}
    for i in range(0, labels.shape[0]):
        digit = int(labels[i].item())
        if digit not in digit_image_dict:
            digit_image_dict[digit] = images[i]  #将当前批次中各数字的第一个存入digit_image_dict

        if len(digit_image_dict.keys()) >= 10:
            break

    # TODO: display target_img with your own student number
    # hint 1: use the images saved in digit_image_dict
    # hint 2: you can use torch.cat() to concatenate digits images to one target_img

    ### CODE START

    target_img = None
    student_id = "2024013325"
    selected_images: list=[]
    for digit in student_id:
        selected_images.append(digit_image_dict[int(digit)])
    target_img=torch.cat(selected_images, dim=2)
    ### CODE END

    target_img = target_img.numpy()
    target_img = target_img.transpose(1, 2, 0)
    display_image(target_img, target_size=240)


