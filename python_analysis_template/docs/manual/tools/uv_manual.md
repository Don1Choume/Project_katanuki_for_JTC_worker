# uv マニュアル

このドキュメントは、Windowsで`uv`を使用するための簡単なマニュアルです。

## インストール

`uv`をインストールするには、PowerShellで次のコマンドを使用します:

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

## 基本的な使い方

- **仮想環境の作成:**

  ```bash
  uv venv
  ```

- **仮想環境のアクティベート:**

  - **PowerShell:**

    ```powershell
    .venv\Scripts\Activate.ps1
    ```

  - **コマンドプロンプト:**

    ```batch
    .venv\Scripts\activate.bat
    ```

- **パッケージの追加 (uv add を使用):**

  `uv`でのパッケージ管理は、必ず`uv add`コマンドを使用してください。`uv pip`コマンドは使用しないでください。

  ```bash
  uv add <パッケージ名>
  ```

  例:
  ```bash
  uv add pandas numpy
  ```

- **requirements.txtからのパッケージのインストール:**

  ```bash
  uv sync
  ```

  または、`requirements.txt`に記載されたパッケージをインストールする場合:
  ```bash
  uv sync -r requirements.txt
  ```

- **パッケージの削除:**

  ```bash
  uv remove <パッケージ名>
  ```

- **requirements.txtの生成:**

  ```bash
  uv freeze > requirements.txt
  ```

- **Jupyter Notebookの起動:**

  仮想環境をアクティベートした後、以下のコマンドでJupyter Notebookを起動できます。

  ```bash
  jupyter notebook
  ```

  Jupyter Notebookがインストールされていない場合は、まず`uv add jupyter`でインストールしてください。

