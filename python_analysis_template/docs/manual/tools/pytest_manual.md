# Pytest マニュアル

このドキュメントは、Pythonプロジェクトで`pytest`を使用してテストを作成および実行するためのマニュアルです。

## 1. Pytestのインストール

`pytest`は`uv`を使用してインストールします。プロジェクトの仮想環境がアクティベートされていることを確認し、以下のコマンドを実行します。

```bash
uv add pytest
```

## 2. テストの実行方法

プロジェクトのルートディレクトリ、またはテストファイルが存在するディレクトリで、以下のコマンドを実行します。

```bash
pytest
```

### よく使うオプション

- `-v` または `--verbose`: 詳細なテスト結果を表示します。
- `-s` または `--capture=no`: テスト中の`print`文などの標準出力を表示します。
- `-k <expression>`: 特定のパターンに一致するテストのみを実行します。
  例: `pytest -k "test_tokenize or TestMyFeature"`
- `-m <marker_expression>`: 特定のマーカーが付与されたテストのみを実行します。
  例: `pytest -m "slow"`
- `--lf` または `--last-failed`: 前回失敗したテストのみを再実行します。
- `--ff` または `--failed-first`: 失敗したテストを最初に実行し、その後残りのテストを実行します。

### 特定のテストファイルの実行

```bash
pytest tests/test_example.py
```

### 特定のテスト関数/メソッドの実行

```bash
pytest tests/test_example.py::test_specific_function
pytest tests/test_example.py::TestClass::test_method
```

## 3. テストのコーディング方法

`pytest`は、シンプルで柔軟なテスト記述を可能にします。

### 3.1. テストファイルの命名規則

- テストファイルは`test_*.py`または`*_test.py`という命名規則に従う必要があります。

### 3.2. テスト関数の記述

- テスト関数は`test_`で始まる必要があります。
- Pythonの標準的な`assert`文を使用してアサーションを行います。

```python
# tests/test_calculations.py

def add(a: int, b: int) -> int:
    return a + b

def test_add_positive_numbers():
    """正の数の加算をテストします。"""
    assert add(1, 2) == 3

def test_add_negative_numbers():
    """負の数の加算をテストします。"""
    assert add(-1, -2) == -3

def test_add_zero():
    """ゼロとの加算をテストします。"""
    assert add(0, 5) == 5
```

### 3.3. テストクラスの記述

- テストクラスは`Test`で始まる必要があります。
- テストメソッドは`test_`で始まる必要があります。

```python
# tests/test_string_operations.py

class StringOperations:
    def reverse(self, s: str) -> str:
        return s[::-1]

    def is_palindrome(self, s: str) -> bool:
        return s == self.reverse(s)

class TestStringOperations:
    """文字列操作クラスのテスト。"""

    def setup_method(self, method):
        """各テストメソッドの実行前に呼ばれます。"""
        self.op = StringOperations()

    def test_reverse_string(self):
        """文字列の反転をテストします。"""
        assert self.op.reverse("hello") == "olleh"

    def test_is_palindrome_true(self):
        """回文である場合のテスト。"""
        assert self.op.is_palindrome("madam") is True

    def test_is_palindrome_false(self):
        """回文でない場合のテスト。"""
        assert self.op.is_palindrome("python") is False
```

### 3.4. Fixture (フィクスチャ)

フィクスチャは、テストのセットアップとティアダウンのコードを再利用可能にするための機能です。`@pytest.fixture`デコレータを使用して定義します。

```python
# tests/conftest.py (フィクスチャは通常conftest.pyに定義します)

import pytest

@pytest.fixture
def sample_data():
    """テスト用のサンプルデータを提供します。"""
    data = [1, 2, 3, 4, 5]
    yield data # テスト実行中にデータを提供
    # yield以降はテスト終了後に実行されるティアダウンコード
    print("\nサンプルデータをクリーンアップしました。")

# tests/test_analysis.py

def test_data_processing(sample_data):
    """サンプルデータを使ったデータ処理をテストします。"""
    processed_data = [x * 2 for x in sample_data]
    assert processed_data == [2, 4, 6, 8, 10]
```

### 3.5. パラメータ化 (Parametrization)

同じテストロジックを異なる入力値で複数回実行したい場合に便利です。`@pytest.mark.parametrize`デコレータを使用します。

```python
# tests/test_math_functions.py

import pytest

def multiply(a: int, b: int) -> int:
    return a * b

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (0, 5, 0),
    (-1, 3, -3),
    (4, -2, -8),
    (-3, -4, 12),
])
def test_multiply(a: int, b: int, expected: int):
    """乗算関数を異なる入力でテストします。"""
    assert multiply(a, b) == expected
```

このマニュアルは、Pytestの基本的な使い方とコーディング方法をカバーしています。より高度な機能については、Pytestの公式ドキュメントを参照してください。

