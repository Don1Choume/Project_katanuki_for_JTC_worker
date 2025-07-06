# -*- coding: utf-8 -*-
"""統計分析の例。
"""

from typing import Tuple

import numpy as np
from scipy import stats

def perform_t_test(sample1: np.ndarray, sample2: np.ndarray) -> Tuple[float, float]:
    """独立した2標本のt検定を実行します。

    Args:
        sample1: NumPy配列としての最初の標本。
        sample2: NumPy配列としての2番目の標本。

    Returns:
        t統計量とp値を含むタプル。
    """
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return t_statistic, p_value
