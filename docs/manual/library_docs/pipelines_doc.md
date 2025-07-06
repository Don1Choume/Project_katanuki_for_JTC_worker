# analysis_lib.pipelines パッケージ

`pipelines`パッケージは、Prefectを使用したデータパイプラインを定義します。

## example_pipeline モジュール

`example_pipeline.py`モジュールは、ETL (Extract, Transform, Load) パイプラインの例を含んでいます。

### フロー: `etl_pipeline`

`etl_pipeline()`

メインのETLパイプラインです。`extract_data`、`transform_data`、`load_data`の3つのタスクを順に実行します。

- **タスク:**
    - `extract_data()`: ソースからデータを抽出します。
    - `transform_data(data)`: 抽出されたデータを変換します。
    - `load_data(data)`: 変換されたデータを宛先にロードします。

- **使用例:**

  ```python
  from analysis_lib.pipelines.example_pipeline import etl_pipeline

  if __name__ == "__main__":
      etl_pipeline()
  ```
