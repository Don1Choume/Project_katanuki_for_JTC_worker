# Python 命名規則マニュアル

このマニュアルは、Pythonのコードを書く際に従うべき命名規則について説明します。主に[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)に基づいています。一貫性のある命名規則に従うことで、コードの可読性が向上し、チーム開発におけるコミュニケーションが円滑になります。

## 1. 基本原則

-   **可読性:** コードは人間が読むために書かれます。命名は、その要素が何であるか、何をするものかを明確に伝えるべきです。
-   **一貫性:** プロジェクト全体で同じ命名規則を適用します。既存のコードベースがある場合は、それに従うことを優先します。
-   **簡潔さ:** 長すぎる名前は避けますが、意味を損なわない範囲で簡潔にします。
-   **英語の使用:** 基本的に英語を使用します。略語は避けるか、広く認知されているもののみを使用します。

## 2. 命名スタイル

PEP 8では、いくつかの命名スタイルが推奨されています。

-   **`lowercase`**: 小文字のみ。
-   **`lower_with_underscore` (snake_case)**: 小文字とアンダースコアで単語を区切る。
-   **`UPPERCASE`**: 大文字のみ。
-   **`UPPER_WITH_UNDERSCORE` (SCREAMING_SNAKE_CASE)**: 大文字とアンダースコアで単語を区切る。
-   **`CapitalizedWords` (CamelCase)**: 各単語の先頭を大文字にする（最初の単語も大文字）。
-   **`mixedCase`**: 最初の単語の先頭は小文字、それ以降の単語の先頭を大文字にする。

## 3. 各要素の命名規則

### 3.1. モジュール (Module)

-   **スタイル:** `lower_with_underscore` (snake_case)
-   **例:** `my_module.py`, `data_processing.py`
-   **注意:** 短く、すべて小文字で、アンダースコアで単語を区切ります。Pythonの予約語や組み込み関数名との衝突を避けます。

### 3.2. パッケージ (Package)

-   **スタイル:** `lowercase` (小文字のみ)
-   **例:** `my_package`, `analysis_lib`
-   **注意:** 短く、すべて小文字で、アンダースコアは使用しません。ディレクトリ名として使用されます。

### 3.3. クラス (Class)

-   **スタイル:** `CapitalizedWords` (CamelCase)
-   **例:** `MyClass`, `UserProfile`, `HttpRequestHandler`
-   **注意:** 略語は避けます。例外として、`HTTP`のような頭字語はすべて大文字で記述しても構いません（例: `HTTPRequestHandler`）。

### 3.4. 関数 (Function) およびメソッド (Method)

-   **スタイル:** `lower_with_underscore` (snake_case)
-   **例:** `my_function()`, `calculate_total()`, `get_user_data()`
-   **注意:** メソッドの最初の引数には、インスタンスメソッドの場合は`self`、クラスメソッドの場合は`cls`を使用します。

### 3.5. 変数 (Variable)

-   **スタイル:** `lower_with_underscore` (snake_case)
-   **例:** `my_variable`, `user_name`, `total_count`
-   **注意:** 短く、意味のある名前にします。ループカウンタなど、一時的な変数には`i`, `j`, `k`のような単一の文字を使用しても構いません。

### 3.6. 定数 (Constant)

-   **スタイル:** `UPPER_WITH_UNDERSCORE` (SCREAMING_SNAKE_CASE)
-   **例:** `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT`, `PI`
-   **注意:** モジュールレベルで定義され、変更されない値に使用します。

### 3.7. 引数 (Arguments)

-   **スタイル:** `lower_with_underscore` (snake_case)
-   **例:** `def process_data(input_data: List[int], output_path: str):`
-   **注意:** 関数やメソッドの引数も変数と同様の規則に従います。

### 3.8. プライベート (Private) およびプロテクテッド (Protected) メンバー

Pythonには厳密なプライベートアクセス修飾子はありませんが、慣習として以下の命名規則が使用されます。

-   **プロテクテッドメンバー:** 単一のアンダースコアで始まる (`_single_leading_underscore`)
    -   **例:** `_internal_method()`, `_private_variable`
    -   **注意:** これは「内部使用のためのヒント」であり、外部からアクセスできないわけではありません。クラスの外部からアクセスすべきではないことを示唆します。

-   **プライベートメンバー (名前マングリング):** 二重のアンダースコアで始まる (`__double_leading_underscore`)
    -   **例:** `__private_method()`, `__secret_data`
    -   **注意:** これはPythonの「名前マングリング」機能を利用したもので、サブクラスでの名前衝突を防ぐために使用されます。厳密なプライベートアクセスを保証するものではありません。

### 3.9. 型変数 (Type Variables)

-   **スタイル:** `CapitalizedWords` (CamelCase) で、単一の文字または短い単語を使用し、通常は`_T`のようなサフィックスを付けます。
-   **例:** `T`, `K`, `V`, `AnyStr`, `_T`
-   **注意:** 型ヒントで使用される`typing.TypeVar`で定義される変数です。

## 4. その他の考慮事項

-   **予約語との衝突:** Pythonの予約語（例: `class`, `def`, `for`, `if`など）や組み込み関数名（例: `list`, `str`, `dict`など）を変数名や関数名に使用しないようにします。どうしても使用する必要がある場合は、末尾にアンダースコアを付けます（例: `class_`, `from_`）。
-   **略語:** 広く認知されている略語（例: `id`, `URL`, `HTTP`）を除き、略語は避けます。完全な単語を使用することで可読性が向上します。
-   **一貫性:** 最も重要なのは一貫性です。プロジェクト内で既に確立されている命名規則がある場合は、それに従うことを優先します。

これらの命名規則に従うことで、より読みやすく、保守しやすいPythonコードを作成することができます。
