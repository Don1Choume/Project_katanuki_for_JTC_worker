# mise マニュアル

このドキュメントは、Windowsで`mise`を使用するための簡単なマニュアルです。

## インストール

`mise`をインストールするには、PowerShellで次のコマンドを使用します:

```powershell
iwr https://mise.run/install.ps1 -useb | iex
```

## 基本的な使い方

- **プロジェクトのローカルPythonバージョンを設定:**

  ```bash
  mise use python@3.11
  ```

  これにより、現在のディレクトリに`.mise.toml`ファイルが作成されます。

- **Shimの実行:**

  `mise`は、正しいツールバージョンを使用するように`PATH`を自動的に管理します。`python`のようなツールを実行すると、`mise`がコマンドをインターセプトし、`.mise.toml`ファイルで指定されたバージョンを実行します。

## バージョン管理

### グローバルバージョンの設定

特定のツールをシステム全体で利用したい場合、`global`コマンドを使用します。

```bash
mise global python@3.11
```

### ローカルバージョンの設定

プロジェクト固有のバージョンを設定するには、プロジェクトのルートディレクトリで`use`コマンドを使用します。これにより、`.mise.toml`ファイルが作成または更新されます。

```bash
mise use python@3.11
```

### 利用可能なバージョンの確認

インストールされているツールとバージョンを確認するには、`ls`コマンドを使用します。

```bash
mise ls
```

### ツールのインストール

特定のツールやバージョンをインストールするには、`install`コマンドを使用します。

```bash
mise install python@3.11
```

## タスクの設定と実行

`mise`では、`.mise.toml`ファイルにカスタムタスクを定義し、実行することができます。これは、プロジェクト固有のスクリプトやコマンドを管理するのに便利です。

### タスクの定義

`.mise.toml`ファイルに`[tasks]`セクションを追加し、その中にタスクを定義します。

例: `run_tests`というタスクを定義し、`pytest`を実行する。

```toml
[tasks]
run_tests = "pytest"
```

### タスクの実行

定義したタスクは`mise run`コマンドで実行できます。

```bash
mise run run_tests
```

### 環境変数の設定

タスク内で環境変数を設定することも可能です。

```toml
[tasks]
build = {
  cmd = "npm run build",
  env = {
    NODE_ENV = "production"
  }
}
```

### 複数のコマンドの実行

タスク内で複数のコマンドを実行する場合は、配列として指定します。

```toml
[tasks]
setup = [
  "npm install",
  "npm run build"
]
```
