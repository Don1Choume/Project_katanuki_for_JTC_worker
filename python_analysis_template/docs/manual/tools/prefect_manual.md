# Prefect マニュアル

このドキュメントは、Pythonプロジェクトで`Prefect`を使用してデータパイプラインを構築および実行するためのマニュアルです。

## 1. Prefectのインストール

`Prefect`は`uv`を使用してインストールします。プロジェクトの仮想環境がアクティベートされていることを確認し、以下のコマンドを実行します。

```bash
uv add prefect
```

## 2. Prefectの基本概念

Prefectの主要な概念は「フロー (Flow)」と「タスク (Task)」です。

- **フロー (Flow):** ワークフロー全体を定義するPython関数です。複数のタスクの実行順序や依存関係をオーケストレーションします。`@flow`デコレータで定義します。
- **タスク (Task):** フロー内で実行される個々の作業単位（例: データの抽出、変換、ロード、モデルのトレーニングなど）を定義するPython関数です。`@task`デコレータで定義します。

## 3. フローの定義

Prefectのフローは、Python関数に`@flow`デコレータを、そのフロー内で実行される個々のステップに`@task`デコレータを付与することで定義します。

```python
# analysis_lib/pipelines/example_pipeline.py

from prefect import flow, task

@task
def extract_data() -> dict:
    """ソースからデータを抽出します。"""
    print("データを抽出中...")
    return {"data": [1, 2, 3, 4, 5]}

@task
def transform_data(data: dict) -> dict:
    """抽出されたデータを変換します。"""
    print("データを変換中...")
    transformed_data = [x * 2 for x in data["data"]]
    return {"transformed_data": transformed_data}

@task
def load_data(data: dict) -> None:
    """変換されたデータを宛先にロードします。"""
    print(f"データをロード中: {data['transformed_data']}")

@flow
def etl_pipeline():
    """メインのETLパイプライン。"""
    extracted_data = extract_data()
    transformed_data = transform_data(extracted_data)
    load_data(transformed_data)

if __name__ == "__main__":
    etl_pipeline()
```

## 4. フローの実行

定義したフローは、Pythonスクリプトとして直接実行できます。上記の`example_pipeline.py`を例にとると、以下のコマンドで実行できます。

```bash
python analysis_lib/pipelines/example_pipeline.py
```

または、`script/run_pipeline.py`のようなCLIスクリプトから実行することもできます。

```bash
python script/run_pipeline.py
```

フローが実行されると、Prefectは実行状況を追跡し、ログを記録します。デフォルトでは、ローカルのSQLiteデータベースにメタデータが保存されます。

## 5. フローのデプロイ (Prefect Cloud/Server)

より堅牢な運用や監視のためには、Prefect Cloudまたはセルフホスト型のPrefect Serverにフローをデプロイすることが推奨されます。

### Prefect Cloudへのログイン

```bash
prefect cloud login
```

### フローのデプロイ

フローをデプロイするには、`prefect deploy`コマンドを使用します。これにより、フローの定義がPrefectのバックエンドに登録され、スケジュール実行や手動実行が可能になります。

```bash
prefect deploy analysis_lib/pipelines/example_pipeline.py:etl_pipeline --name my-first-etl-flow
```

デプロイ後、Prefect UI (Prefect CloudまたはPrefect Server) からフローの実行状況を監視したり、スケジュールを設定したりできます。

## 6. その他の主要な機能

- **リトライ (Retries):** タスクが失敗した場合に自動的に再試行する設定が可能です。
- **キャッシング (Caching):** タスクの出力をキャッシュし、同じ入力で再実行された場合にタスクをスキップすることで、パイプラインの実行時間を短縮できます。
- **ロギング (Logging):** Prefectは、フローとタスクの実行中に詳細なログを自動的に収集します。
- **パラメータ化 (Parameters):** フローにパラメータを定義し、実行時に異なる入力値を渡すことができます。

より詳細な情報や高度な機能については、Prefectの公式ドキュメントを参照してください。
