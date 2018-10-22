import numpy as np
import cv2
# MatplotlibはPythonのデータの可視化用ライブラリで，様々なデータの可視化方法を提供する
from matplotlib import pyplot as plt

# 画像読み込み
# 第1引数は画像のファイルパス
# 第2引数は画像の読み込み方法を指定するためのフラグ
# cv2.IMREAD_COLOR 1 : カラー画像として読み込む．画像の透明度は無視される．デフォルト値
# cv2.IMREAD_GRAYSCALE  0 : グレースケール画像として読み込む
# cv2.IMREAD_UNCHANGED -1 : アルファチャンネルも含めた画像として読み込む
img = cv2.imread('C://Users/takasugi/Pictures/cat.JPG', cv2.IMREAD_GRAYSCALE)


# 指定したwindowサイズで見たい場合
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 画像の表示
cv2.imshow('image', img)

# キーボード入力を処理する
# 引数で渡した時間だけ待機する。0を指定すると無制限に待機
cv2.waitKey(0)

# cv2.destroyAllWindows() は現在までに作られた全てのウィンドウを閉じる関数です．
# 特定のウィンドウのみを閉じる場合は cv2.destroyWindow() 関数に閉じたいウィンドウ名を指定してください
cv2.destroyAllWindows()