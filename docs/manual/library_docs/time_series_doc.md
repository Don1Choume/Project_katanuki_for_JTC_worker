# analysis_lib.time_series パッケージ

`time_series`パッケージは、時系列分析機能を提供します。

## analysis モジュール

`analysis.py`モジュールは、時系列データの移動平均を計算する関数を含んでいます。

### 関数: `calculate_moving_average`

`calculate_moving_average(time_series, window)`

時系列データの移動平均を計算します。

- **引数:**
    - `time_series` (`pd.Series`): Pandas Seriesとしての入力時系列データ。
    - `window` (`int`): 移動ウィンドウのサイズ。

- **戻り値:**
    - `pd.Series`: Pandas Seriesとしての時系列データの移動平均。

- **使用例:**

  ```python
  import pandas as pd
  from analysis_lib.time_series.analysis import calculate_moving_average

  data = pd.Series([10, 12, 11, 13, 15, 14, 16, 17, 18, 20])
  window_size = 3

  moving_avg = calculate_moving_average(data, window_size)
  print(f"移動平均: {moving_avg}")
  ```
