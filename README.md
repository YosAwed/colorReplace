# colorReplace
任意のPNGファイルを読み込み、JSONファイルで指定された色を対応する色に変換する


# プログラムの概要
PNGファイルの読み込み: Pillowライブラリを使用してPNG画像を読み込みます。
JSONファイルの読み込み: JSONファイルから色マップ（元の色と変換後の色のペア）を取得します。
ピクセルの変換: 画像の各ピクセルをチェックし、JSONの色マップに基づいて色を変換します。
画像の保存: 変換後の画像を新しいPNGファイルとして保存します。

# 前提条件
Python 3.xがインストールされている。
Pillowライブラリがインストールされている（pip install Pillowでインストール）。

JSONファイルは以下のような形式：
sample.json
{
    "color_map": [
        {"original": [255, 0, 0], "replacement": [0, 0, 255]},
        {"original": [0, 255, 0], "replacement": [255, 255, 0]}
    ]
}

ここでは、RGB値をリストとして表し、originalが元の色、replacementが変換後の色を示します。

# 注意点
画像モード: PNGファイルがRGBAの場合、RGBに変換しています。JSONの色データがRGBAに対応している場合は、変換処理を調整する必要があります。
パフォーマンス: 大きな画像ではループ処理が遅くなる可能性があります。その場合、NumPyを使用した最適化を検討してください。

# 実行方法
ターミナルで以下のコマンドを実行します：

python color_replace.py input.png sample.json

変換が成功すると、input_converted.pngが出力され、完了メッセージが表示されます。




