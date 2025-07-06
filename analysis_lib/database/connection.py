# -*- coding: utf-8 -*-
"""データベース操作の例。
"""

import sqlite3
from typing import List, Tuple

def execute_query(db_path: str, query: str) -> List[Tuple]:
    """SQLiteデータベースに対してクエリを実行します。

    Args:
        db_path: SQLiteデータベースへのパス。
        query: 実行するSQLクエリ。

    Returns:
        クエリ結果を表すタプルのリスト。
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
