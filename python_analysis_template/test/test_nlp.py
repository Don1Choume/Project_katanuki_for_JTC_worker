# -*- coding: utf-8 -*-
"""ユニットテストの例。
"""

import unittest

from analysis_lib.nlp.preprocessing import tokenize

class TestTokenize(unittest.TestCase):
    """tokenize関数をテストします。
    """

    def test_tokenize(self):
        """tokenize関数が文章を単語に分割することをテストします。
        """
        sentence = "これはテストの文章です。"
        expected_tokens = ["これは", "テストの", "文章です。"]
        actual_tokens = tokenize(sentence)
        self.assertEqual(expected_tokens, actual_tokens)

if __name__ == "__main__":
    unittest.main()
