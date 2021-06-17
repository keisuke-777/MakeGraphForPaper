import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
import csv


def plot(
    index,
    element,
    element_num,
    x_range,
    y_range,
    label_name,
    interval,
    name_list,
    disp_legend,
    legend_location,
    color_list,
):
    plt.rcParams["legend.edgecolor"] = "black"  # edgeの色を変更
    plt.rcParams["font.family"] = "IPAexGothic"
    plt.rcParams["xtick.direction"] = "in"  # x軸の目盛線：内向き('in')、外向き('out')、双方向('inout')
    plt.rcParams["ytick.direction"] = "in"  # y軸の目盛線
    plt.rcParams["xtick.major.width"] = 1.0  # x軸主目盛り線の線幅
    plt.rcParams["ytick.major.width"] = 1.0  # y軸主目盛り線の線幅
    plt.rcParams["font.size"] = 10  # フォントの大きさ
    plt.rcParams["axes.linewidth"] = 1.0  # 囲みの太さ

    plt.grid(True)  # グリッド線(格子状になってる線)の有無

    plt.locator_params(axis="x", nbins=11)  # x軸，11個以内
    plt.locator_params(axis="y", nbins=11)  # y軸，11個以内

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax.set_xlim(x_range[0], x_range[1])  # x軸の表示範囲
    ax.set_ylim(y_range[0], y_range[1])  # y軸の表示範囲

    # 目盛りの表示間隔の指定
    if interval != 0:
        ax.xaxis.set_ticks(np.arange(0, x_range[1] + 1, x_range[1] // interval))

    ax.set_xlabel(label_name[0], fontsize=18)  # x軸のラベル名
    ax.set_ylabel(label_name[1], fontsize=18)  # y軸のラベル名

    left = index
    for i in range(element_num):
        height = element[i]
        # グラフの色を編集する場合は->を参考にするのがおすすめ(https://matplotlib.org/2.0.2/examples/color/named_colors.html)
        ax.plot(left, height, label=name_list[i], color=color_list[i])

    if disp_legend:
        plt.legend(fontsize=16, loc=legend_location)  # 凡例の記載
    plt.show()


# csvファイルのパス、読み込んで欲しいインデックスの数、プロットする要素数
def csvReader(
    csv_pass,
    index_num,
    element_num,
    x_range,
    y_range,
    label_name,
    interval=0,
    name_list=["no_name"],
    disp_legend=True,
    legend_location="lower right",
    color_list=["b", "g", "r", "c", "m", "y", "k", "w"],
):
    index = np.array([0] * index_num)
    element = []
    for _ in range(element_num):
        el = np.array([0.0] * index_num)
        element.append(el)

    csv_input = pd.read_csv(filepath_or_buffer=csv_pass, encoding="ms932", sep=",")
    for i, row in enumerate(csv_input.values):
        index[i] = int(row[0])
        for element_index in range(element_num):
            element[element_index][i] = float(row[element_index + 1])

    plot(
        index,
        element,
        element_num,
        x_range,
        y_range,
        label_name,
        interval,
        name_list,
        disp_legend,
        legend_location,
        color_list,
    )


# 動作確認
if __name__ == "__main__":
    # 例1
    # csvReader(
    #     csv_pass="./data/one.csv",
    #     index_num=40,
    #     element_num=1,
    #     x_range=[1, 40],
    #     y_range=[0, 1],
    #     label_name=["x_label_name", "y_label_name"],
    #     interval=4,
    #     disp_legend=False,
    #     color_list=["#ff7f00"],
    # )

    # 例2
    csvReader(
        csv_pass="./data/two.csv",
        index_num=40,
        element_num=2,
        x_range=[0, 360],
        y_range=[0, 1],
        label_name=["ラベル太郎", "ラベル次郎"],
        interval=8,
        name_list=["data1", "data2"],
        disp_legend=True,
        legend_location="upper right",
    )

    # 例3
    # csvReader(
    #     csv_pass="./data/three.csv",
    #     index_num=50,
    #     element_num=3,
    #     x_range=[0, 500],
    #     y_range=[0, 500],
    #     label_name=["ラベルくん", "ラベルさん"],
    #     interval=0,
    #     name_list=["データA", "データB", "データC"],
    #     disp_legend=True,
    #     legend_location="lower left",
    #     color_list=["y", "k", "m"],
    # )
