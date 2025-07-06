# analysis_lib.llm パッケージ

`llm`パッケージは、大規模言語モデル (LLM) との連携機能を提供します。

## generation モジュール

`generation.py`モジュールは、LLMを使用してテキストを生成する関数を含んでいます。

### 関数: `generate_text`

`generate_text(prompt)`

大規模言語モデルを使用してテキストを生成します。

- **引数:**
    - `prompt` (`str`): 入力プロンプト。

- **戻り値:**
    - `str`: 生成されたテキスト。

- **使用例:**

  ```python
  from analysis_lib.llm.generation import generate_text

  prompt = "Pythonでデータ分析を行うための最初のステップは何ですか？"
  generated_response = generate_text(prompt)
  print(f"生成された応答: {generated_response}")
  ```
