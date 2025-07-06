# マニュアル目次

この目次では、プロジェクトで使用される各種マニュアルの概要とリンクを提供します。

## 1. ツール関連マニュアル

プロジェクトで使用する主要なツールに関するマニュアルです。

-   **[mise マニュアル](tools/mise_manual.md)**
    -   `mise`のインストール方法、Pythonバージョン管理、タスク設定と実行方法について説明します。
-   **[uv マニュアル](tools/uv_manual.md)**
    -   `uv`のインストール方法、仮想環境の管理、パッケージの追加・削除、Jupyter Notebookの起動方法について説明します。
-   **[Prefect マニュアル](tools/prefect_manual.md)**
    -   `Prefect`のインストール、基本概念（フロー、タスク）、フローの定義と実行、デプロイ方法について説明します。
-   **[Pytest マニュアル](tools/pytest_manual.md)**
    -   `pytest`のインストール、テストの実行方法、テストのコーディング方法（関数、クラス、フィクスチャ、パラメータ化）について説明します。

## 2. 方法論関連マニュアル

プロジェクトの開発プロセスやベストプラクティスに関するマニュアルです。

-   **[プロジェクト開始とフォルダ活用マニュアル](methodologies/getting_started_manual.md)**
    -   プロジェクトの初期セットアップ、フォルダ構造と各フォルダの活用方法、`analysis_lib`の概要について説明します。
-   **[Git-flow マニュアル](methodologies/git_flow_manual.md)**
    -   Git-flowブランチモデルの基本、Issueとの関連付け、マージリクエスト/プルリクエストの対応について説明します。
-   **[GitHub Flow マニュアル](methodologies/github_flow_manual.md)**
    -   GitHub Flowブランチモデルの基本、Issueとの関連付け、プルリクエストの対応について説明します。
-   **[Python 命名規則マニュアル](methodologies/python_naming_conventions_manual.md)**
    -   PEP 8に基づいたPythonの命名規則について、各要素（モジュール、クラス、関数、変数など）の命名スタイルと具体例を説明します。
-   **[TDD (テスト駆動開発) マニュアル](methodologies/tdd_manual.md)**
    -   TDDの概念、Red-Green-Refactorサイクル、和田卓人氏のTDDへの強調点、実践例について初心者向けに詳しく説明します。

## 3. ライブラリドキュメント

`analysis_lib`内の各モジュールや関数の詳細な説明と使用例です。

-   **[audio パッケージ](library_docs/audio_doc.md)**
    -   音声信号からの特徴量抽出 (`extract_features`) について説明します。
-   **[database パッケージ](library_docs/database_doc.md)**
    -   SQLiteデータベースへのクエリ実行 (`execute_query`) について説明します。
-   **[evaluation パッケージ](library_docs/evaluation_doc.md)**
    -   分類モデルの精度計算 (`calculate_accuracy`) について説明します。
-   **[graph パッケージ](library_docs/graph_doc.md)**
    -   グラフ内の最短経路探索 (`find_shortest_path`) について説明します。
-   **[llm パッケージ](library_docs/llm_doc.md)**
    -   大規模言語モデルによるテキスト生成 (`generate_text`) について説明します。
-   **[nlp パッケージ](library_docs/nlp_doc.md)**
    -   テキストのトークン化 (`tokenize`) について説明します。
-   **[optimize パッケージ](library_docs/optimize_doc.md)**
    -   勾配降下法による最適化 (`gradient_descent`) について説明します。
-   **[pipelines パッケージ](library_docs/pipelines_doc.md)**
    -   Prefectを使用したETLパイプラインの例 (`etl_pipeline`) について説明します。
-   **[signal パッケージ](library_docs/signal_doc.md)**
    -   信号へのフィルタ適用 (`apply_filter`) について説明します。
-   **[statistics パッケージ](library_docs/statistics_doc.md)**
    -   独立2標本のt検定 (`perform_t_test`) について説明します。
-   **[time_series パッケージ](library_docs/time_series_doc.md)**
    -   時系列データの移動平均計算 (`calculate_moving_average`) について説明します。
-   **[utils パッケージ](library_docs/utils_doc.md)**
    -   ロガーの作成と設定 (`get_logger`) について説明します。
-   **[vision パッケージ](library_docs/vision_doc.md)**
    -   画像のサイズ変更 (`resize_image`) について説明します。
-   **[visualize パッケージ](library_docs/visualize_doc.md)**
    -   ヒストグラムのプロット (`plot_histogram`) について説明します。
