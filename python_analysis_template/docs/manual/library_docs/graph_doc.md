# analysis_lib.graph パッケージ

`graph`パッケージは、グラフ分析機能を提供します。

## analysis モジュール

`analysis.py`モジュールは、グラフ内の最短経路を見つける関数を含んでいます。

### 関数: `find_shortest_path`

`find_shortest_path(graph, source, target)`

グラフ内の2つのノード間の最短経路を見つけます。

- **引数:**
    - `graph` (`networkx.Graph`): NetworkXグラフとしての入力グラフ。
    - `source` (`str`): 開始ノード。
    - `target` (`str`): ターゲットノード。

- **戻り値:**
    - `List[str]`: ノードのリストとしての最短経路。

- **使用例:**

  ```python
  import networkx as nx
  from analysis_lib.graph.analysis import find_shortest_path

  G = nx.Graph()
  G.add_edges_from([('A', 'B'), ('B', 'C'), ('A', 'C'), ('C', 'D')])

  path = find_shortest_path(G, 'A', 'D')
  print(f"最短経路: {path}")
  ```
