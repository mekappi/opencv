import cv2
import matplotlib.pyplot as plt
import pyautogui
import numpy as np


def getRectByPoints(points):
    points = list(map(lambda x: x[0], points))

    points = sorted(points, key=lambda x:x[1])
    top_points = sorted(points[:2], key=lambda x:x[0])
    bottom_points = sorted(points[2:4], key=lambda x:x[0])
    points = top_points + bottom_points

    left = min(points[0][0], points[2][0])
    right = max(points[1][0], points[3][0])
    top = min(points[0][1], points[1][1])
    bottom = max(points[2][1], points[3][1])
    return (top, bottom, left, right)


def getPartImageByRect(rect):
    img = cv2.imread(image_dir + image_file, 1)
    return img[rect[0]:rect[1], rect[2]:rect[3]]


# 物体検知
image_dir = 'C://Users/takasugi/Desktop/'
image_file = 'sample.jpg'

im = cv2.imread(image_dir + image_file, 1)
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# ガウシアンフィルタを用いて画像の平滑化を行います．
im_blur = cv2.GaussianBlur(im_gray, (11,11), 0)

im_test = (np.abs(im[:, :, 2] - im[:, :, 1]) + np.abs(im[:, :, 2] - im[:, :, 0]))
im_test2 = (np.abs(im[:, :, 0] - im[:, :, 1]) + np.abs(im[:, :, 0] - im[:, :, 1]))

# 2値化：閾値の一定値より上なら黒、下なら白といったような
# INVは反転
# 画素値が閾値より大きければある値(白色)を割り当て，そうでなければ別の値(黒色)を割り当てる。
ret1, th1 = cv2.threshold(im_blur, 127, 255, cv2.THRESH_BINARY_INV)
# 配列に対して，適応的な閾値処理を行います．
th2 = cv2.adaptiveThreshold(im_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)
th = cv2.threshold(im_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
th4 = cv2.threshold(im_gray + im_blur + im_test, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
th5 = cv2.threshold(im_gray + im_test, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
th6 = cv2.threshold(im_gray + im_test2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


cv2.imshow('test', th6)
while True:
    k = cv2.waitKey(1)
    if k == 27:
        break

# 2値画像中の輪郭を検出します
contours = cv2.findContours(th6, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
th_area = im.shape[0] * im.shape[1] / 100
# 輪郭が囲む領域の面積を求めます
contours_large = list(filter(lambda c:cv2.contourArea(c) > th_area, contours))

outputs = []
rects = []
approxes = []

for (i, cnt) in enumerate(contours_large):
    # arcLength : 輪郭線の周囲長，あるいは曲線の長さを求めます．
    arclen = cv2.arcLength(cnt, True)
    # approxPolyDP : 折れ線（カーブ）を指定された精度で近似します
    approx = cv2.approxPolyDP(cnt, 0.02 * arclen, True)
    if len(approx) < 4:
        continue
    approxes.append(approx)
    rect = getRectByPoints(approx)
    rects.append(rect)
    outputs.append(getPartImageByRect(rect))
    cv2.imwrite('./output' + str(i) + '.jpg', getPartImageByRect(rect))


