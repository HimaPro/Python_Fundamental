# 自作パッケージの作り方


## ファイル構造
```
mypackage/ 
  __init__.py
  mod1.py
  mod2.py
main.py
```
mypackage: モジュールを格納するパッケージ用のディレクトリ  
  __init__.py: パッケージのインポート設定  
  mod1.py: モジュール1を記述したファイル  
  mod2.py: モジュール2を記述したファイル  
main.py: 実行するメインのプログラム  


## ファイルの中身
```main.py
from mypackage import *
```
