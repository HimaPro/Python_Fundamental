import cv2
from PIL import Image, ImageTk


# 画像をモノクロ画像に変換
def img2otsu(img):
    ''' BGR画像 --> モノクロ画像'''
    ret, dst = cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_OTSU)
    
    return dst


# cv2画像をPIL画像に変換
def cv2pil(image):
    ''' OpenCV型 -> PIL型 '''
    new_image = image.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)
    return new_image


# cv2画像をTKinterで使える画像に変換
def cv2_to_tk(cv2_image):
    'CV2 -> Tkinter'
    # BGR -> RGB
    rgb_cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

    # NumPy配列からPIL画像オブジェクトを生成
    pil_image = Image.fromarray(rgb_cv2_image)

    # PIL画像オブジェクトをTkinter画像オブジェクトに変換
    tk_image = ImageTk.PhotoImage(pil_image)

    return tk_image


# 横幅に合わせて画像を拡大・縮小
def scale_to_width(img, width=200):
    ''' cv2 image --> scaled image '''
    h, w = img.shape[:2]
    amp = width / w
    height = round(h * amp)
    dst = cv2.resize(img, dsize=(width, height))

    return dst


# 横幅に合わせて画像を拡大・縮小
def scale_to_height(img, height=200):
    ''' cv2 image --> scaled image '''
    h, w = img.shape[:2]
    amp = height / h
    width = round(w * amp)
    dst = cv2.resize(img, dsize=(width, height))

    return dst