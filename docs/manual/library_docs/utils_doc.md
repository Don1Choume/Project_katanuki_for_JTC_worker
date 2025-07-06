# analysis_lib.utils パッケージ

`utils`パッケージは、汎用的なユーティリティ関数を提供します。

## logging モジュール

`logging.py`モジュールは、ロガーを作成および設定する関数を含んでいます。

### 関数: `get_logger`

`get_logger(name, level=logging.INFO)`

ロガーを作成し、設定します。

- **引数:**
    - `name` (`str`): ロガーの名前。
    - `level` (`int`, オプション): ロギングレベル。デフォルトは`logging.INFO`。

- **戻り値:**
    - `logging.Logger`: 設定済みのロガーインスタンス。

- **使用例:**

  ```python
  from analysis_lib.utils.logging import get_logger
  import logging

  logger = get_logger("my_application", level=logging.DEBUG)
  logger.debug("これはデバッグメッセージです。")
  logger.info("これは情報メッセージです。")
  logger.warning("これは警告メッセージです。")
  ```
