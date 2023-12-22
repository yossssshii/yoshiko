import cv2
import numpy as np
from matplotlib import pyplot as plt

def calculate_dark_ratio(image_path):
    # 画像の読み込み
    img_bw = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 一定の敷居値(今回は120)より暗い箇所のみ表示
    img_bw_m = np.where(img_bw < 120, 1, 0)

    # 暗い箇所の割合の計算
    dark_ratio = np.sum(img_bw_m) / (img_bw.shape[0] * img_bw.shape[1]) * 100
    
    # 有効数字3桁に丸める
    dark_ratio = round(dark_ratio, 3)

    return dark_ratio


def fill_dark_regions(image_path, threshold=120, border_color=(238, 104, 123), fill_color=(219, 112, 147, 255), border_thickness=4):
    # 画像の読み込み
    img = cv2.imread(image_path)

    # グレースケールに変換
    img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 一定の敷居値より暗い箇所を抽出
    dark_regions = np.where(img_bw < threshold, 1, 0).astype(np.uint8)

    # 輪郭を検出
    contours, _ = cv2.findContours(dark_regions, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 輪郭内を指定した色で塗りつぶし
    img_with_filled_dark_regions = np.zeros_like(img, dtype=np.uint8)
    cv2.drawContours(img_with_filled_dark_regions, contours, -1, (219, 112, 147), thickness=cv2.FILLED)

    # 輪郭の線をLightSeaGreenで太く描画
    cv2.drawContours(img_with_filled_dark_regions, contours, -1, border_color[:3], thickness=border_thickness)

    # 元の画像の暗部以外の部分を白で残す
    img_with_filled_dark_regions[dark_regions == 0, :] = img[dark_regions == 0, :]

    # 保存先のパス
    output_path = 'static/image_with_filled_dark_regions.png'
    cv2.imwrite(output_path, img_with_filled_dark_regions)

    return output_path













