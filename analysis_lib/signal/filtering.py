# -*- coding: utf-8 -*-
"""信号処理の例。
"""

import numpy as np

def apply_filter(signal: np.ndarray, filter_coefficients: np.ndarray) -> np.ndarray:
    """信号にフィルタを適用します。

    Args:
        signal: NumPy配列としての入力信号。
        filter_coefficients: NumPy配列としてのフィルタ係数。

    Returns:
        NumPy配列としてのフィルタ処理された信号。
    """
    # これは実際のフィルタ実装のプレースホルダーです。
    # 例: scipy.signal.lfilterを使用する場合
    print("信号にフィルタを適用しています。")
    return np.convolve(signal, filter_coefficients, mode='same')
