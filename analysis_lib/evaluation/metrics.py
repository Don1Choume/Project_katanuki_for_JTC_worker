# -*- coding: utf-8 -*-
"""モデル評価関数。
"""

from typing import Tuple

import numpy as np

def calculate_accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """分類モデルの精度を計算します。

    Args:
        y_true: 真のラベル。
        y_pred: 予測されたラベル。

    Returns:
        モデルの精度。
    """
    return np.mean(y_true == y_pred)
