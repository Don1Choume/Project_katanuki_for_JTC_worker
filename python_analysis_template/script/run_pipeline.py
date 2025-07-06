# -*- coding: utf-8 -*-
"""コマンドラインスクリプトの例。
"""

import argparse

from analysis_lib.pipelines.example_pipeline import etl_pipeline

def main():
    """コマンドラインスクリプトのメイン関数。
    """
    parser = argparse.ArgumentParser(description="ETLパイプラインを実行します。")
    parser.parse_args()

    print("コマンドラインからETLパイプラインを開始します...")
    etl_pipeline()
    print("ETLパイプラインが完了しました。")

if __name__ == "__main__":
    main()
