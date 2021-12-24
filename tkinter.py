# https://daeudaeu.com/tkinter_canvas_draw/#width
# -*- coding:utf-8 -*-
import tkinter
import cv2
from PIL import Image, ImageTk

press_flag = False

def cv2_to_tk(cv2_image):
    'CV2 -> Tkinter'

    # BGR -> RGB
    rgb_cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

    # NumPy配列からPIL画像オブジェクトを生成
    pil_image = Image.fromarray(rgb_cv2_image)

    # PIL画像オブジェクトをTkinter画像オブジェクトに変換
    tk_image = ImageTk.PhotoImage(pil_image)

    return tk_image


app = tkinter.Tk()

canvas = tkinter.Canvas(
    app,
    width=600,
    height=300,
    background="white"
)
canvas.pack()

IMG = cv2.imread("genwaku_map8.jpg")
photo_image = cv2_to_tk(IMG)

# キャンバスのサイズを取得
canvas_width = canvas.winfo_width()
canvas_height = canvas.winfo_height()

# 画像の描画
canvas.create_image(
    # 画像表示位置(Canvasの中心)
    canvas_width / 2,
    canvas_height / 2,

    # 表示画像データ
    image = photo_image,
    )

# https://daeudaeu.com/tkinter_canvas_draw/#dashoffset
# active:カーソルが載ってる状態
# カーソルが外れると通常の値になる

# 楕円・円を描画
canvas.create_oval(
    # 長方形に接する形で楕円が描画される
    50, 50,
    100, 100,

    # タグ
    tag="rect_1",

    #塗りつぶしの色を設定
    fill="orange",
    activefill="red",
    disabledfill="pink",

    #枠線の太さ
    width=20,
    activewidth=10,
    disabledwidth=5,

    #枠線の色
    outline="blue",
    activeoutline="green",
    disabledoutline="brown",

    #枠線を破線にする(線の長さ,空白の長さ)
    dash=(10,5),
    activedash=(20,5),
    disableddash=(10,3),

    # tkinter.NORMAL:通常, tkinter.DISABLED:無効, tkinter.HIDDEN:非表示
    state=tkinter.NORMAL,
    )

# 多角形を描画
canvas.create_polygon(
    # 長方形に接する形で楕円が描画される
    50, 50,
    100, 100,
    150, 120,
    200, 70,

    # タグ
    tag="rect_1",

    #枠線の太さ
    width=20,
    activewidth=10,
    disabledwidth=5,

    #枠線の色
    outline="blue",
    activeoutline="green",
    disabledoutline="brown",

    # tkinter.NORMAL:通常, tkinter.DISABLED:無効, tkinter.HIDDEN:非表示
    state=tkinter.NORMAL,

    #色を設定
    fill="orange",
    activefill="red",
    disabledfill="pink",

    #枠線を破線にする(線の長さ,空白の長さ)
    dash=(10,5),
    activedash=(20,5),
    disableddash=(10,3),
    )

# 直線を描画(矢印も追加可能)
canvas.create_line(
    # 長方形に接する形で楕円が描画される
    50, 50,
    100, 100,
    150, 120,
    200, 70,

    # タグ
    tag="rect_1",

    #枠線の太さ
    width=20,
    activewidth=10,
    disabledwidth=5,

    #枠線の色
    outline="blue",
    activeoutline="green",
    disabledoutline="brown",

    # tkinter.NORMAL:通常, tkinter.DISABLED:無効, tkinter.HIDDEN:非表示
    state=tkinter.NORMAL,

    #色を設定
    fill="orange",
    activefill="red",
    disabledfill="pink",

    #枠線を破線にする(線の長さ,空白の長さ)
    dash=(10,5),
    activedash=(20,5),
    disableddash=(10,3),

    # tkinter.NONE:矢印なし, tkinter.FIRST:最初の点に矢印, tkinter.LAST:最後の点に矢印, tkinter.BOTH:両端に矢印
    arrow=tkinter.BOTH

    # 矢じりの形(棒から矢印の先端 < やじりの後ろの長さ, 矢じりの幅)
    arrowshape=(20,20,10)
    )

# 円弧を描画
canvas.create_arc(
    # 基準となる長方形
    50, 50,
    100, 100,

    # 始点と終点の角度
    start=30,
    extent=90,

    # タグ
    tag="rect_1",

    # tkinter.ARC:円弧, tkinter.PIESLICE:扇形(デフォルト), tkinter.CHORD:弦(弓矢のような形)
    style=tkinter.ARC

    #枠線の太さ
    width=20,
    activewidth=10,
    disabledwidth=5,

    #枠線の色
    outline="blue",
    activeoutline="green",
    disabledoutline="brown",

    # tkinter.NORMAL:通常, tkinter.DISABLED:無効, tkinter.HIDDEN:非表示
    state=tkinter.NORMAL,

    #色を設定
    fill="orange",
    activefill="red",
    disabledfill="pink",

    #枠線を破線にする(線の長さ,空白の長さ)
    dash=(10,5),
    activedash=(20,5),
    disableddash=(10,3),
    )

# テキストを描画
canvas.create_text(
    # 基準位置の配置場所
    100, 100

    # テキスト
    text="ここに文章を入力"

    font=
    # タグ
    tag="rect_1",

    # 基準位置の設定
    # tkinter.CENTER:中央(デフォルト), tkinter.N:上, tkinter.E:右, tkinter.NW:左上, tkinter.SE:右下
    anchor=tkinter.SW
    
    #塗りつぶしの色を設定
    fill="orange",
    activefill="red",
    disabledfill="pink",

    #枠線の太さ
    width=20,
    activewidth=10,
    disabledwidth=5,

    # tkinter.NORMAL:通常, tkinter.DISABLED:無効, tkinter.HIDDEN:非表示
    state=tkinter.NORMAL,
)

app.mainloop()
