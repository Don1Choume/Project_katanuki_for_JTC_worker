# analysis_lib.optimize パッケージ

`optimize`パッケージは、最適化アルゴリズムの実装を提供します。

## gradient_descent モジュール

`gradient_descent.py`モジュールは、勾配降下法の実装を含んでいます。

### 関数: `gradient_descent`

`gradient_descent(objective_function, gradient_function, initial_point, learning_rate=0.01, num_iterations=100)`

勾配降下法を用いて目的関数を最小化します。

- **引数:**
    - `objective_function` (`Callable[[np.ndarray], float]`): 最小化する目的関数。NumPy配列を入力とし、floatを返します。
    - `gradient_function` (`Callable[[np.ndarray], np.ndarray]`): 目的関数の勾配を計算する関数。NumPy配列を入力とし、NumPy配列を返します。
    - `initial_point` (`np.ndarray`): 最適化の開始点となるNumPy配列。
    - `learning_rate` (`float`, オプション): 学習率。デフォルトは0.01。
    - `num_iterations` (`int`, オプション): 繰り返しの回数。デフォルトは100。

- **戻り値:**
    - `Tuple[np.ndarray, list]`: 最適化された点と、各イテレーションでの目的関数の値のリストを含むタプル。

- **使用例:**

  ```python
  import numpy as np
  from analysis_lib.optimize.gradient_descent import gradient_descent

  # 目的関数: f(x) = x^2
  def f(x: np.ndarray) -> float:
      return x[0]**2

  # 勾配関数: f'(x) = 2x
  def df(x: np.ndarray) -> np.ndarray:
      return np.array([2 * x[0]])

  initial_x = np.array([10.0])
  optimized_x, loss_history = gradient_descent(f, df, initial_x, learning_rate=0.1, num_iterations=50)

  print(f"最適化された点: {optimized_x}")
  print(f"最終的な目的関数の値: {loss_history[-1]}")
  ```
