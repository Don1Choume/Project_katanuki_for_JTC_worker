# analysis_lib.evaluation パッケージ

`evaluation`パッケージは、モデル評価のためのメトリクスを提供します。

## metrics モジュール

`metrics.py`モジュールは、分類モデルの精度を計算する関数を含んでいます。

### 関数: `calculate_accuracy`

`calculate_accuracy(y_true, y_pred)`

分類モデルの精度を計算します。

- **引数:**
    - `y_true` (`np.ndarray`): 真のラベル。
    - `y_pred` (`np.ndarray`): 予測されたラベル。

- **戻り値:**
    - `float`: モデルの精度。

- **使用例:**

  ```python
  import numpy as np
  from analysis_lib.evaluation.metrics import calculate_accuracy

  y_true = np.array([0, 1, 0, 1, 0])
  y_pred = np.array([0, 1, 1, 1, 0])

  accuracy = calculate_accuracy(y_true, y_pred)
  print(f"モデルの精度: {accuracy}")
  ```
