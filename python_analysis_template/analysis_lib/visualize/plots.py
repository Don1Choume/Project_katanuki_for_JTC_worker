# -*- coding: utf-8 -*-
"""可視化関数。
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(data: np.ndarray, bins: int = 10, title: str = "ヒストグラム") -> None:
    """与えられたデータのヒストグラムをプロットします。

    Args:
        data: NumPy配列としてプロットするデータ。
        bins: ヒストグラムのビンの数。
        title: ヒストグラムのタイトル。
    """
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.xlabel("値")
    plt.ylabel("頻度")
    plt.show()
