import cv2
import numpy as np

# 線分を引くために必要なnp.arrayを出力する 
def poly_data(data):
    pts = np.array(data,dtype=np.int32)
    return [pts]

if __name__ == "__main__":
	img = cv2.imread("test.txt")
	
	data = [[10,10],[40,80],[20,60]]
	pts = poly_data(data)
	cv2.polylines(img,pts,False,(0,0,255),3)
	
	
	
	# ポリラインを描画
	cv2.polylines(img,
		      pts,			# 描画位置
		      isClosed = True/False,	# True:閉じる, False:閉じない
		      color = (0, 0, 255),	# (B, G, R)
		      thickness = 3,		# 線の太さ(int)
		      lineType = cv2.LINE_8	# cv2.LINE_4 / cv2.LINE_8(デフォルト) / cv2.LINE_AA(くっきり)
		     )

  
	# マーカーを描画
	cv2.drawMarker(img,
		       position = (x, y),		# 描画位置
		       color = (0, 0, 255),		# (B, G, R)
		       markerType = cv2.MARKER_CROSS,	# マーカーの形
		       markerSize = 20,			# サイズ
		       thickness = 1,			# 太さ(int)
		       lineType = cv2.LINE_8		# cv2.LINE_4 / cv2.LINE_8(デフォルト) / cv2.LINE_AA(くっきり)
		      )
	
	# markerType
	# MARKER_CROSS : ✖
	# MARKER_TILTED_CROSS : ✙
	# MARKER_STAR : ★
	# MARKER_DIAMOND : 🔹
	# MARKER_SQUARE : ■
	# MARKER_TRIANGLE_UP : ▲
	# MARKER_TRIANGLE_DOWN : ▼

	
	# 四角形を描画
	cv2.rectangle(img,
		      pt1,			# (100, 200)
		      pt2,			# (200, 300)
		      color=(B,G,R),		# (B, G, R)
		      thickness = 1,		# 太さ(-1:塗りつぶし)(int)
		      lineType = cv2.LINE_8,	# cv2.LINE_4 / cv2.LINE_8(デフォルト) / cv2.LINE_AA(くっきり)
		      shift = 0			# 小数点の指定？
		     )
	
	# 円を描画
	cv2.circle(img,
		   center = (x,y), 		# 描画位置
		   radius = 60, 		# 半径
		   color = (0, 0, 255),		# (B, G, R)
		   thickness = int(value), 	# 線の太さ(-1:塗りつぶし)
		   lineType = cv2.LINE_8,	# cv2.LINE_4 / cv2.LINE_8(デフォルト) / cv2.LINE_AA(くっきり)
		   shift = 0
		  )

	
	# 直線を引く
	cv2.line(img,
		 pt1,			# (100, 200)
		 pt2,			# (200, 300)
		 color=(B,G,R),		# (B, G, R)
		 thickness = 1,		# 線の太さ(int)
		 lineType = cv2.LINE_8	# cv2.LINE_4 / cv2.LINE_8(デフォルト) / cv2.LINE_AA(くっきり)
		)

	
	# 矢印を描画
	cv2.arrowedLine(img,
			pt1,			# (100, 200)
		 	pt2,			# (200, 300)
		 	color=(B,G,R),		# (B, G, R)
		 	thickness = 3,		# 線の太さ(int)
		 	lineType = cv2.LINE_8,	# cv2.LINE_4 / cv2.LINE_8(デフォルト) / cv2.LINE_AA(くっきり)
			shift = 0,		# 小数点の指定？
			tipLength = 0.1 	#(全体に対する矢の部分の割合)
		       )

	
	# テキストを描画
	cv2.putText(img,
		    text = “This is the text”,			# 表示テキスト
		    org = (x,y),				# 左下の位置
		    fontFace = cv2.FONT_HERSHEY_SIMPLEX,	# フォントを選択	
		    fontScale = float(value),			# 1を基準にしてフォントの大きさ
		    color = (0, 0, 255),			# (B, G, R)
		    thickness = 3,				# 線の太さ(int)
		    lineType = cv2.LINE_8	# cv2.LINE_4 / cv2.LINE_8(デフォルト) / cv2.LINE_AA(くっきり)
		   )

	# fontFace
	# cv2.FONT_HERSHEY_SIMPLEX
	# cv2.FONT_HERSHEY_PLAIN
	# cv2.FONT_HERSHEY_DUPLEX
	# cv2.FONT_HERSHEY_COMPLEX
	# cv2.FONT_HERSHEY_TRIPLEX
	# cv2.FONT_HERSHEY_COMPLEX_SMALL
	# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
	# cv2.FONT_HERSHEY_SCRIPT_COMPLEX
	# cv2.FONT_ITALIC
