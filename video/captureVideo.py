import numpy as np
import cv2

# 動画撮影オブジェクト
# 引数はデバイス番号 カメラが1台しか接続されていなければ0で指定される
cap = cv2.VideoCapture(0)

if not(cap.isOpened()):
    print("カメラの初期化に失敗しました。")
    exit()

# 動画の情報を取得
# idの詳細はhttps://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get
print(cap.get(3)) # 幅
print(cap.get(4)) # 高さ
print(cap.get(5)) # FPS

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()