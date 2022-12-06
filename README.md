# moon
いろんな検索エンジンを素早く使い分けよう。
<img width="1136" alt="スクリーンショット 2022-12-06 1 07 27" src="https://user-images.githubusercontent.com/88177671/205685066-d6012c26-2a77-4333-8842-c7cf5c5092b5.png">

## About moon.
元々簡易的な Webkit のブラウザが欲しかった。  
Python で GUI を書くときに wxPython の経験があったので、その技術を流用してちょっとしたアプリを作ろう、という思考にたどり着いた。

このブラウザの面白いところは、Google, Bing, Yahoo, DuckDuckGo といった有名な検索エンジンを素早く使い分けることができるという点。  

検索結果は検索エンジンによって異なることが多い。  
簡単に好みのエンジンで検索できるのは割と便利だと思う。  

また、余計な検索バーを用意していない点も一つの特徴だ。  
そのため全画面表示にしたとき表示領域が広がって非常に見通しが良い。  


## Build
ビルドするには <code>pyinstaller</code> が必要です。
```
pyinstaller moon.py --onefile --noconsole --icon=web/icon.png
```

## License
まだ未定。
