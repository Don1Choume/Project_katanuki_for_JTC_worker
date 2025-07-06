# analysis_lib.visualize パッケージ

`visualize`パッケージは、データ可視化機能を提供します。

## plots モジュール

`plots.py`モジュールは、ヒストグラムをプロットする関数を含んでいます。

### 関数: `plot_histogram`

`plot_histogram(data, bins=10, title="ヒストグラム")`

与えられたデータのヒストグラムをプロットします。

- **引数:**
    - `data` (`np.ndarray`): NumPy配列としてプロットするデータ。
    - `bins` (`int`, オプション): ヒストグラムのビンの数。デフォルトは10。
    - `title` (`str`, オプション): ヒストグラムのタイトル。デフォルトは"ヒストグラム"。

- **使用例:**

  ```python
  import numpy as np
  from analysis_lib.visualize.plots import plot_histogram

  sample_data = np.random.randn(1000) # 正規分布に従う1000個のデータ
  plot_histogram(sample_data, bins=30, title="ランダムデータのヒストグラム")
  ```
