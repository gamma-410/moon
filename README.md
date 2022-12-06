<h3 align="center"><b>moon</b></h3>
<p align="center">
<code>ミニマムなWebブラウザ</code>
</p>
<img width="1136" alt="スクリーンショット 2022-12-06 1 07 27" src="https://user-images.githubusercontent.com/88177671/205685066-d6012c26-2a77-4333-8842-c7cf5c5092b5.png">

<hr>
<br>

## ✨ 特徴
- Python製 (wxPython)
- wx.html2.WebViewレンダリング
- 検索バーが無いので見通しが良い
- 検索エンジンを素早く使い分けることができる

<br>
<hr>
<br>

## 🌱 なぜ作ったのか?
元々、簡易的なブラウザが欲しかった。  
Python で GUI を書くときに wxPython の利用経験があり、  
「その技術を流用してちょっとしたアプリを作ろう」という思考にたどり着いた。

<br>
<hr>
<br>

## 🔨 ビルド
ビルドするには <code>pyinstaller</code> が必要です。
```
pyinstaller moon.py --onefile --noconsole --icon=web/icon.png
```
<br>
<hr>
<br>

## 📝 ライセンス
まだ未定。
