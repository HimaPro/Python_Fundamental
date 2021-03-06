# 自作パッケージの作り方

[参考にしたサイト](https://dev.classmethod.jp/articles/python-create-package/)

## ファイル構造
```
main.py

mypackage/ 
    
  __init__.py
  mod1.py
  mod2.py
  
  alpha/
    mod3.py
    mod4.py
```
mypackage: モジュールを格納するパッケージ用のディレクトリ  
  alpha: 種類ごとにまとめたディレクトリ
  __init__.py: パッケージのインポート設定  
  mod1.py: モジュール1を記述したファイル  
  mod2.py: モジュール2を記述したファイル  
main.py: 実行するメインのプログラム  

<br>

## ファイルの中身
```py
# main.py
from mypackage import *

double(3) # 3*2を出力
three() # => "mod3 is called"
```

<br>

```py
# __init__.py
from mypackage.mod1 import *
from mypackage.mod2 import *

# mypackageは省略可
from .alpha.mod3 import *
from .alpha.mod4 import * 
```

```py
# mod1.py
def double(n):
    print(n*2)
```

```py
# mod2.py
def square(n):
    print(n**2)
```

```py
# alpha/mod3.py
def three():
    print("mod3 is called")
```

```py
# alpha/mod4.py
def four():
    print("mod4 is called")
```

<br>

## パッケージのインストール方法
mypackageのフォルダを使用するPython.exeと同じ階層にあるLibフォルダに保存する。
`C:\Users\userA\AppData\Local\Programs\Python\Python310\Lib`
![パッケージ](https://user-images.githubusercontent.com/95124230/174756915-a8d368c1-a1a6-4989-87c2-b06ee8bf8443.png)

<br>

## インストールしない場合
インストールをしなくてもmain.pyと同じ階層にパッケージが保存されていれば同じように使うことは可能。  
最終変更前はこのようにローカルから実行したほうがいいかも？
