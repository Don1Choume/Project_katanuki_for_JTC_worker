# GitHub Flow マニュアル

このドキュメントでは、GitHub Flowのブランチモデルについて説明します。

## 基本原則

- **`main`ブランチのコードは常にデプロイ可能であること。**
- **新しい作業を始めるときは、`main`から説明的な名前のブランチを作成します (例: `new-oauth-scopes`)。**
- **ローカルでそのブランチにコミットし、定期的にサーバー上の同じ名前のブランチに作業をプッシュします。**
- **フィードバックや助けが必要なとき、またはブランチがマージの準備ができたと思ったときは、プルリクエストを開きます。**
- **機能がレビューされ承認されたら、`main`にマージできます。**
- **一度`main`にマージされてプッシュされたら、すぐにデプロイできますし、そうすべきです。**

## Issueとの関連付け

GitHub Flowでは、プルリクエストとIssueを密接に連携させることが推奨されます。プルリクエストの本文やコミットメッセージに`Fixes #123`や`Closes #456`のようにIssue番号を記述することで、プルリクエストがマージされた際に自動的にIssueをクローズすることができます。

## プルリクエスト (Pull Request) の対応

### 作成

- 新しい機能やバグ修正のためのブランチで作業が完了したら、`main`ブランチへのプルリクエストを作成します。
- プルリクエストのタイトルは、変更内容を簡潔に表すものにします。
- プルリクエストの本文には、以下の情報を記載します。
    - **変更の目的:** なぜこの変更が必要なのか。
    - **変更内容:** 具体的に何を変更したのか。
    - **テスト方法:** どのようにテストしたのか、またはどのようにテストできるのか。
    - **関連するIssue:** 関連するIssueがあれば、`#Issue番号`の形式で記載します。
    - **スクリーンショット/動画:** UIの変更がある場合は、視覚的な情報を提供します。

### レビュー

- プルリクエストが作成されたら、チームメンバーがコードレビューを行います。
- レビュー担当者は、コードの品質、設計、テスト、ドキュメントなどを確認し、コメントや提案を行います。
- レビューコメントに対応し、必要に応じてコードを修正し、再度プッシュします。これにより、プルリクエストは自動的に更新されます。

### マージ

- 少なくとも1人以上のレビュー担当者から承認 (Approve) を得たら、プルリクエストを`main`ブランチにマージできます。
- マージ方法は、通常「Squash and Merge」または「Rebase and Merge」が推奨されます。これにより、`main`ブランチのコミット履歴がクリーンに保たれます。
- マージ後、関連するIssueが自動的にクローズされたことを確認します。

### デプロイ

- `main`ブランチにマージされた変更は、すぐに本番環境にデプロイされるべきです。これにより、継続的なデリバリーが実現されます。
