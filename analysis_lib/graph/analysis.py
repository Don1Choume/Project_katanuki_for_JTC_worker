# -*- coding: utf-8 -*-
"""グラフ分析の例。
"""

from typing import Dict, List

import networkx as nx

def find_shortest_path(graph: nx.Graph, source: str, target: str) -> List[str]:
    """グラフ内の2つのノード間の最短経路を見つけます。

    Args:
        graph: NetworkXグラフとしての入力グラフ。
        source: 開始ノード。
        target: ターゲットノード。

    Returns:
        ノードのリストとしての最短経路。
    """
    return nx.shortest_path(graph, source=source, target=target)
