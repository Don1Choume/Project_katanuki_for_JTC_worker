# -*- coding: utf-8 -*-
"""ユーティリティ関数。
"""

import logging

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """ロガーを作成し、設定します。

    Args:
        name: ロガーの名前。
        level: ロギングレベル。

    Returns:
        設定済みのロガーインスタンス。
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
