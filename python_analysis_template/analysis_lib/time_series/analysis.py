# -*- coding: utf-8 -*-
"""時系列分析の例。
"""

import pandas as pd

def calculate_moving_average(time_series: pd.Series, window: int) -> pd.Series:
    """時系列データの移動平均を計算します。

    Args:
        time_series: Pandas Seriesとしての入力時系列データ。
        window: 移動ウィンドウのサイズ。

    Returns:
        Pandas Seriesとしての時系列データの移動平均。
    """
    return time_series.rolling(window=window).mean()
