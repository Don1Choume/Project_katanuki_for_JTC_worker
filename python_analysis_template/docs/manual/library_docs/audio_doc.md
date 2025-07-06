# analysis_lib.audio パッケージ

`audio`パッケージは、音声処理機能を提供します。

## feature_extraction モジュール

`feature_extraction.py`モジュールは、音声信号から特徴量を抽出する関数を含んでいます。

### 関数: `extract_features`

`extract_features(audio_signal, sample_rate)`

音声信号から特徴量を抽出します。

- **引数:**
    - `audio_signal` (`np.ndarray`): NumPy配列としての入力音声信号。
    - `sample_rate` (`int`): 音声信号のサンプルレート。

- **戻り値:**
    - `np.ndarray`: NumPy配列としての抽出された特徴量。

- **使用例:**

  ```python
  import numpy as np
  from analysis_lib.audio.feature_extraction import extract_features

  # サンプル音声信号 (例: 1秒間の44.1kHzのモノラル信号)
  sample_rate = 44100
  duration = 1  # seconds
  t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
  audio_signal = 0.5 * np.sin(2 * np.pi * 440 * t) # 440Hzのサイン波

  features = extract_features(audio_signal, sample_rate)
  print(f"抽出された特徴量の形状: {features.shape}")
  ```
