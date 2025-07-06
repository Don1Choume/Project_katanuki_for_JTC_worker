# -*- coding: utf-8 -*-
"""最適化アルゴリズムの例。
"""

import numpy as np
from typing import Callable, Tuple

def gradient_descent(objective_function: Callable[[np.ndarray], float],
                     gradient_function: Callable[[np.ndarray], np.ndarray],
                     initial_point: np.ndarray,
                     learning_rate: float = 0.01,
                     num_iterations: int = 100) -> Tuple[np.ndarray, list]:
    """勾配降下法を用いて目的関数を最小化します。

    Args:
        objective_function: 最小化する目的関数。NumPy配列を入力とし、floatを返します。
        gradient_function: 目的関数の勾配を計算する関数。NumPy配列を入力とし、NumPy配列を返します。
        initial_point: 最適化の開始点となるNumPy配列。
        learning_rate: 学習率。デフォルトは0.01。
        num_iterations: 繰り返しの回数。デフォルトは100。

    Returns:
        最適化された点と、各イテレーションでの目的関数の値のリストを含むタプル。
    """
    current_point = initial_point
    history = [objective_function(current_point)]

    for i in range(num_iterations):
        gradient = gradient_function(current_point)
        current_point = current_point - learning_rate * gradient
        history.append(objective_function(current_point))

    return current_point, history


# 使用例
if __name__ == "__main__":
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

    # 目的関数: f(x, y) = (x-1)^2 + (y-2)^2
    def g(xy: np.ndarray) -> float:
        return (xy[0] - 1)**2 + (xy[1] - 2)**2

    # 勾配関数: g'(x, y) = [2(x-1), 2(y-2)]
    def dg(xy: np.ndarray) -> np.ndarray:
        return np.array([2 * (xy[0] - 1), 2 * (xy[1] - 2)])

    initial_xy = np.array([5.0, 5.0])
    optimized_xy, loss_history_xy = gradient_descent(g, dg, initial_xy, learning_rate=0.1, num_iterations=50)

    print(f"最適化された点 (多変数): {optimized_xy}")
    print(f"最終的な目的関数の値 (多変数): {loss_history_xy[-1]}")
