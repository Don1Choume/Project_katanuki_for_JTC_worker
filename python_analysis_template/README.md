# Python分析プロジェクトテンプレート

**注記:** 本リポジトリは、日本の伝統的な大企業（JTC）に勤務するデータ分析従事者向けに、Gemini CLIを用いて試験的に作成・一部改変されたものです。詳細な説明は`docs/manual`フォルダを参照してください。

これはデータ分析用のPythonプロジェクトのテンプレートです。

## フォルダ構成

- **config/**: 設定ファイル。gitの管理対象外。
- **docs/**: ドキュメント。
  - **manual/**: ツールやワークフローのマニュアル。
  - **rule/**: プロジェクトのルール。
  - **plan/**: プロジェクトの計画。
  - **presentation/**: プレゼンテーション資料。
  - **report/**: レポート。
  - **reference/**: 参考資料。
- **data/**: データファイル。gitの管理対象外。
  - **row/**: 生データ。
  - **interim/**: 中間データ。
  - **processed/**: 加工済みデータ。
  - **external/**: 外部データ。
  - **models/**: 学習済みモデル。
- **result/**: 分析結果。gitの管理対象外。
  - **fig/**: 図やプロット。
  - **interm/**: 中間結果。
  - **output/**: 最終出力。
- **note/**: テストや探索的分析用のJupyter Notebook。
- **test/**: ユニットテスト。
- **script/**: コマンドライン実行用のスクリプト。
- **analysis_lib/**: プロジェクト固有のライブラリコード。
  - **config/**: 設定の読み込み。
  - **pipelines/**: データ処理パイプライン (Prefectを使用)。
  - **etl/**: ETL (Extract, Transform, Load) スクリプト。
  - **ml/**: 機械学習モデル。
  - **analysis/**: 分析スクリプト。
  - **nlp/**: 自然言語処理。
  - **vision/**: コンピュータビジョン。
  - **signal/**: 信号処理。
  - **audio/**: 音声処理。
  - **time_series/**: 時系列分析。
  - **graph/**: グラフ分析。
  - **llm/**: 大規模言語モデル。
  - **statistics/**: 統計分析。
  - **database/**: データベースとの連携。
  - **utils/**: ユーティリティ関数。
  - **visualize/**: 可視化関数。
  - **evaluation/**: モデル評価。

## セットアップ

このプロジェクトでは、Pythonのバージョン管理に`mise`、パッケージ管理に`uv`を使用します。

1.  `mise`と`uv`をインストールします。詳細は`docs/manual`のマニュアルを参照してください。
2.  `mise use python@3.11` を実行してPythonのバージョンを設定します。
3.  `uv pip install -r requirements.txt` を実行して必要なパッケージをインストールします。(注: `requirements.txt`はまだ作成されていません)
