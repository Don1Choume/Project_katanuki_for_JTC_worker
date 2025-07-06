# -*- coding: utf-8 -*-
"""自然言語処理の例。
"""

from typing import List

def tokenize(sentence: str) -> List[str]:
    """文章を単語に分割します。

    Args:
        sentence: 入力文。

    Returns:
        トークンのリスト。
    """
    # ここでは単純にスペースで分割していますが、
    # 実際の形態素解析ではMeCabやJanomeなどを使用します。
    return sentence.split()
