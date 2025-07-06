# analysis_lib.nlp パッケージ

`nlp`パッケージは、自然言語処理機能を提供します。

## preprocessing モジュール

`preprocessing.py`モジュールは、テキストの前処理関数を含んでいます。

### 関数: `tokenize`

`tokenize(sentence)`

文章を単語に分割します。

- **引数:**
    - `sentence` (`str`): 入力文。

- **戻り値:**
    - `List[str]`: トークンのリスト。

- **使用例:**

  ```python
  from analysis_lib.nlp.preprocessing import tokenize

  text = "これはテストの文章です。"
  tokens = tokenize(text)
  print(f"トークン化された単語: {tokens}")
  ```
