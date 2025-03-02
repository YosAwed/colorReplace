import json
import sys
import os
from PIL import Image


def replace_colors(image_path, json_path):
    """
    PNGファイルのピクセル色をJSONファイルに基づいて変換し、出力ファイル名を自動生成する関数。
    
    Args:
        image_path (str): 入力PNGファイルのパス
        json_path (str): 色マップを含むJSONファイルのパス
    """
    # JSONファイルを読み込む
    try:
        with open(json_path, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"エラー: JSONファイル '{json_path}' が見つかりません。")
        return
    except json.JSONDecodeError:
        print(f"エラー: JSONファイル '{json_path}' の形式が不正です。")
        return
    
    # 色マップを辞書形式に変換（RGB値をタプルとして扱う）
    color_map = {
        tuple(item["original"]): tuple(item["replacement"])
        for item in json_data["color_map"]
    }
    
    # PNG画像を読み込む
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"エラー: PNGファイル '{image_path}' が見つかりません。")
        return
    except Exception as e:
        print(f"エラー: PNGファイル '{image_path}' の読み込みに失敗しました。詳細: {e}")
        return
    
    # 画像がRGBAモードの場合、RGBに変換
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    # ピクセルデータにアクセス
    pixels = image.load()
    width, height = image.size
    
    # 各ピクセルをチェックして色を変換
    for y in range(height):
        for x in range(width):
            current_color = pixels[x, y]  # 現在のピクセルの色（RGBタプル）
            if current_color in color_map:
                pixels[x, y] = color_map[current_color]  # 変換後の色に変更
    
    # 出力ファイル名を生成（例: input.png -> input_converted.png）
    base_name = os.path.splitext(image_path)[0]  # 拡張子を除いたファイル名
    output_path = f"{base_name}_converted.png"
    
    # 変換後の画像を保存
    image.save(output_path)
    print(f"画像の色変換が完了しました。出力ファイル: {output_path}")

# コマンドライン引数の処理
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用法: python color_replace.py <PNGファイル> <JSONファイル>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    json_path = sys.argv[2]
    
    replace_colors(image_path, json_path)

