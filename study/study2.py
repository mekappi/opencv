import cv2
# import matplotlib.pyplot as plt
import pyautogui

cap = cv2.VideoCapture(0)

global avg
avg = None
# 動体検知
# 1.背景画像を取得

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if avg is None:
        avg = gray.copy().astype("float")
        continue

    cv2.accumulateWeighted(gray, avg, 0.1)
    # 差分を取得
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))

    cv2.imshow('Raw Frame', frameDelta)

    #前フレームとの比較
    #avg = gray.copy().astype("float")

    print(pyautogui.position())
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
