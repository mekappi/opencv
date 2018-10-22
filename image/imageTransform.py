import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C://Users/takasugi/Pictures/cat.JPG', cv2.IMREAD_COLOR)
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

# 指定したwindowサイズで見たい場合
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 画像の表示
cv2.imshow('image', res)

# キーボード入力を処理する
# 引数で渡した時間だけ待機する。0を指定すると無制限に待機
cv2.waitKey(0)

# cv2.destroyAllWindows() は現在までに作られた全てのウィンドウを閉じる関数です．
# 特定のウィンドウのみを閉じる場合は cv2.destroyWindow() 関数に閉じたいウィンドウ名を指定してください
cv2.destroyAllWindows()