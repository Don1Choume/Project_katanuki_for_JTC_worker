# analysis_lib.signal パッケージ

`signal`パッケージは、信号処理機能を提供します。

## filtering モジュール

`filtering.py`モジュールは、信号にフィルタを適用する関数を含んでいます。

### 関数: `apply_filter`

`apply_filter(signal, filter_coefficients)`

信号にフィルタを適用します。

- **引数:**
    - `signal` (`np.ndarray`): NumPy配列としての入力信号。
    - `filter_coefficients` (`np.ndarray`): NumPy配列としてのフィルタ係数。

- **戻り値:**
    - `np.ndarray`: NumPy配列としてのフィルタ処理された信号。

- **使用例:**

  ```python
  import numpy as np
  from analysis_lib.signal.filtering import apply_filter

  # サンプル信号とフィルタ係数
  signal = np.array([1, 2, 3, 4, 5])
  filter_coeffs = np.array([0.5, 0.5]) # 移動平均フィルタの例

  filtered_signal = apply_filter(signal, filter_coeffs)
  print(f"フィルタ処理された信号: {filtered_signal}")
  ```
