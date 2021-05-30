import rondom

import cv2
import numpy

def cut_patch(img):
    img_height, img_width, _ = img.shape
    top = random.randrange(0, round(img_height))
    bottom = top + random.randrange(round(img_height*0.05),
                                            round(img_height*0.15))
    left = random.randrange(0, round(img_width))
    right = left + random.randrange(round(img_width*0.05),
                                            round(img_width*0.15))
    if (bottom - top) % 2 == 1:
        bottom -= 1
    if (right - left) % 2 == 1:
        right -= 1
    return img[top:bottom, left:right, :]

def paste_patch(img, patch, rot, ratio):
    img_height, img_width, _ = img.shape
    patch_height, patch_width, _ = patch.shape
    width_half = round(img_width / 2)
    height_half = round(img_height / 2)
    trans_x = random.randrange(-width_half, width_half)
    trans_y = random.randrange(-height_half, height_half)
    patch_h_center = round(patch_height / 2)
    patch_w_center = round(patch_width / 2)
    img_h_center = round(img_height / 2)
    img_w_center = round(img_width / 2)
    top = round((img_height - patch_height) / 2)
    bottom = round((img_height + patch_height) / 2)
    left = round((img_width - patch_width) / 2)
    right = round((img_width + patch_width) / 2)
    # paste on center
    tmp_img = np.zeros((img_height, img_width, 3), np.uint8)
    tmp_img[top:bottom, left:right, :] = patch
    # rotation and expansion
    M = cv2.getRotationMatrix2D((img_w_center, img_h_center), rot, ratio)
    tmp_img = cv2.warpAffine(tmp_img, M, (img_width, img_height))
    # translation
    M = np.float32([[1, 0, trans_x], [0, 1, trans_y]])
    tmp_img = cv2.warpAffine(tmp_img, M, (img_width, img_height))
    # make mask of patch
    imggray = cv2.cvtColor(tmp_img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(imggray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # cut the mask from original image
    back = cv2.bitwise_and(img, img, mask=mask_inv)
    cut = cv2.bitwise_and(tmp_img, tmp_img, mask = mask)
    # paste(combine original and patch)
    paste = cv2.add(back, cut)
    return paste
