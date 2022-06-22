import pyocr
from .color import cv2pil
import os


def ocr_text(img):
    ''' cv2画像(img2otsu()したもの) --> 認識した文字 '''
    
    path = 'C:\\Program Files\\Tesseract-OCR'
    os.environ['PATH'] = os.environ['PATH'] + path

    pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    # pyocrへ利用するOCRエンジンをTesseractに指定する。
    tools = pyocr.get_available_tools()
    tool = tools[0]
    
    # OCR対象の画像ファイルを読み込む
    # img_binary_INV = Image.open(filename)
    img_binary_INV = cv2pil(img)
    
    # 画像から文字を読み込む
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    text = tool.image_to_string(img_binary_INV, lang="eng", builder=builder)
    
    print(text)
    text.replace(".", "")
    
    conversion_list = {
        "g": "9",
        "/": "7",
        "O": "Q",
    }
    
    if text[0] in ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]:
        return text[0]
    elif text == "10":
        return text
    elif text in conversion_list:
        return conversion_list[text]
    
    return "None"