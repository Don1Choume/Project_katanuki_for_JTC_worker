# analysis_lib.statistics パッケージ

`statistics`パッケージは、統計分析機能を提供します。

## hypothesis_testing モジュール

`hypothesis_testing.py`モジュールは、仮説検定関数を含んでいます。

### 関数: `perform_t_test`

`perform_t_test(sample1, sample2)`

独立した2標本のt検定を実行します。

- **引数:**
    - `sample1` (`np.ndarray`): NumPy配列としての最初の標本。
    - `sample2` (`np.ndarray`): NumPy配列としての2番目の標本。

- **戻り値:**
    - `Tuple[float, float]`: t統計量とp値を含むタプル。

- **使用例:**

  ```python
  import numpy as np
  from analysis_lib.statistics.hypothesis_testing import perform_t_test

  sample_a = np.array([10, 12, 11, 13, 15])
  sample_b = np.array([8, 9, 10, 11, 12])

  t_statistic, p_value = perform_t_test(sample_a, sample_b)
  print(f"T統計量: {t_statistic}, P値: {p_value}")
  ```
