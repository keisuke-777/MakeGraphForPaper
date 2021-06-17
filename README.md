# MakeGraphForPaper

matplotlibを使ってグラフを作成する際のテンプレートです。気が向いたらREADMEを見やすくします。

# 使い方

csvReaderに適切な引数を入れてあげます。

## 引数の説明
- csv_pass：読み込ませたいcsvのパス
- index_num：読み込ませたいデータの要素数（行数）
- element_num：読み込ませたいデータの要素の種類数（列数+1）
- x_range：x軸の表示範囲
- y_range：y軸の表示範囲
- label_name：x軸、y軸のラベル名のリスト
- interval：x軸の目盛りを何個に区切るか（未入力であれば適宜分割）
- name_list：凡例の名前のリスト（凡例を入力しない場合は不要）
- disp_legend：凡例を表示するかどうか（未入力であれば表示）
- legend_location：凡例をどこに表示するか（未入力であれば右下に表示）
- color_list：グラフ要素の色のリスト（未入力であれば青、緑、赤...と自動で割り振られる）