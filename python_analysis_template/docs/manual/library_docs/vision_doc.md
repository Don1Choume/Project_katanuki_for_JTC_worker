# analysis_lib.vision パッケージ

`vision`パッケージは、コンピュータビジョン機能を提供します。

## preprocessing モジュール

`preprocessing.py`モジュールは、画像の前処理関数を含んでいます。

### 関数: `resize_image`

`resize_image(image, size)`

画像を特定のサイズに変更します。

- **引数:**
    - `image` (`np.ndarray`): NumPy配列としての入力画像。
    - `size` (`Tuple[int, int]`): タプル(幅, 高さ)としての画像の希望サイズ。

- **戻り値:**
    - `np.ndarray`: NumPy配列としてのリサイズされた画像。

- **使用例:**

  ```python
  import numpy as np
  from analysis_lib.vision.preprocessing import resize_image

  # ダミー画像データ (例: 高さ100, 幅150, 3チャンネルの画像)
  dummy_image = np.zeros((100, 150, 3), dtype=np.uint8)
  target_size = (200, 200) # 幅, 高さ

  resized_image = resize_image(dummy_image, target_size)
  print(f"リサイズされた画像の形状: {resized_image.shape}")
  ```
