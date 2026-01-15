import pyxel

def update():
    # ゲームの状態を更新する処理
    pass

def draw():
    # 画面に描画する処理
    pyxel.cls(0) # 画面を黒でクリア
    pyxel.text(60, 50, "Hello, Pyxel!", pyxel.rndi(0, 7)) # テキストを描画 (X座標, Y座標, テキスト, 色)

pyxel.init(160, 120) # 画面サイズを160x120ピクセルに設定
pyxel.run(update, draw) # ゲームを実行
