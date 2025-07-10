# Ruffとuv環境での利用マニュアル

## 1. はじめに

このマニュアルは、高速なPythonリンター＆フォーマッターであるRuffを、`uv`パッケージマネージャー環境下でセットアップし、利用する方法について解説します。

## 2. Ruffとは

RuffはRustで書かれた非常に高速なPythonリンターです。Flake8、isort、pyupgradeなど、数十のツールの機能を単一のCLIで提供します。設定がシンプルで、既存のプロジェクトにも導入しやすいのが特徴です。

## 3. `uv`環境へのRuffの導入

### 3.1. インストール

`uv`がプロジェクトのパッケージマネージャーとして設定されている場合、以下のコマンドでRuffを開発依存関係として追加します。

```bash
# 開発依存関係としてインストール
uv pip install --dev ruff
```

これにより、`pyproject.toml`にRuffが追記され、`uv.lock`が更新されます。

### 3.2. `pyproject.toml`での設定

Ruffの挙動は、プロジェクトルートの`pyproject.toml`ファイルで管理するのが一般的です。

以下は設定例です。

```toml
[tool.ruff]
# isortやflake8などのルールセットを有効にする
# ルール一覧: https://docs.astral.sh/ruff/rules/
select = ["E", "F", "W", "I", "UP"]
ignore = []

# 1行の最大文字数
line-length = 88

# 除外するファイルやディレクトリ
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

[tool.ruff.lint]
# isort (importの自動ソート) の設定
[tool.ruff.lint.isort]
known-first-party = ["analysis_lib"] # プロジェクトのソースディレクトリを指定

[tool.ruff.format]
# Black互換のフォーマットを有効にする
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
```

## 4. Ruffの実行

### 4.1. Lint（静的解析）

プロジェクト全体のコードをチェックするには、以下のコマンドを実行します。

```bash
uv run ruff check .
```

修正可能な違反は、`--fix`オプションを付けることで自動修正できます。

```bash
uv run ruff check . --fix
```

### 4.2. Format（コードフォーマット）

プロジェクト全体のコードをフォーマットするには、以下のコマンドを実行します。

```bash
uv run ruff format .
```

## 5. 使い方

1.  コードを記述します。
2.  `uv run ruff format .` を実行して、コードスタイルを統一します。
3.  `uv run ruff check . --fix` を実行して、Lintエラーのチェックと自動修正を行います。
4.  残ったLintエラーを手動で修正します。

このフローをCI/CDパイプラインやpre-commitフックに組み込むことで、コードの品質を常に高く保つことができます。
