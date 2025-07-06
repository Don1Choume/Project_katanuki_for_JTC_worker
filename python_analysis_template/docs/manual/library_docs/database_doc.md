# analysis_lib.database パッケージ

`database`パッケージは、データベースとの連携機能を提供します。

## connection モジュール

`connection.py`モジュールは、SQLiteデータベースに対するクエリ実行関数を含んでいます。

### 関数: `execute_query`

`execute_query(db_path, query)`

SQLiteデータベースに対してクエリを実行します。

- **引数:**
    - `db_path` (`str`): SQLiteデータベースへのパス。
    - `query` (`str`): 実行するSQLクエリ。

- **戻り値:**
    - `List[Tuple]`: クエリ結果を表すタプルのリスト。

- **使用例:**

  ```python
  import sqlite3
  from analysis_lib.database.connection import execute_query

  # テスト用のデータベースを作成
  db_path = "/tmp/test.db"
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
  cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
  cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
  conn.commit()
  conn.close()

  # クエリを実行
  results = execute_query(db_path, "SELECT * FROM users WHERE age > 28")
  print(f"クエリ結果: {results}")
  ```
