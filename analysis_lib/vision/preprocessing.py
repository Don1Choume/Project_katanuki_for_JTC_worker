# -*- coding: utf-8 -*-
"""コンピュータビジョン処理の例。
"""

from typing import Tuple

import numpy as np

def resize_image(image: np.ndarray, size: Tuple[int, int]) -> np.ndarray:
    """画像を特定のサイズに変更します。

    Args:
        image: NumPy配列としての入力画像。
        size: タプル(幅, 高さ)としての画像の希望サイズ。

    Returns:
        NumPy配列としてのリサイズされた画像。
    """
    # これは実際の画像リサイズ実装のプレースホルダーです。
    # 例: OpenCVを使用する場合: cv2.resize(image, size)
    print(f"画像を{size}にリサイズしています")
    return np.zeros((size[1], size[0], image.shape[2]), dtype=image.dtype)
