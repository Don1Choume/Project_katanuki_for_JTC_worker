# -*- coding: utf-8 -*-
"""Prefectパイプラインの例。
"""

from prefect import flow, task

@task
def extract_data() -> dict:
    """ソースからデータを抽出します。

    Returns:
        抽出されたデータを含む辞書。
    """
    print("データを抽出中...")
    return {"data": [1, 2, 3, 4, 5]}

@task
def transform_data(data: dict) -> dict:
    """抽出されたデータを変換します。

    Args:
        data: 変換するデータ。

    Returns:
        変換されたデータを含む辞書。
    """
    print("データを変換中...")
    transformed_data = [x * 2 for x in data["data"]]
    return {"transformed_data": transformed_data}

@task
def load_data(data: dict) -> None:
    """変換されたデータを宛先にロードします。

    Args:
        data: ロードするデータ。
    """
    print(f"データをロード中: {data['transformed_data']}")

@flow
def etl_pipeline():
    """メインのETLパイプライン。
    """
    extracted_data = extract_data()
    transformed_data = transform_data(extracted_data)
    load_data(transformed_data)

if __name__ == "__main__":
    etl_pipeline()
