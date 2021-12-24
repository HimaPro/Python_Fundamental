import networkx as nx

def shortest_path():
	# グラフデータを作成
    G = nx.Graph()
	
	# グラフにノード間の重みを定義
    G.add_weighted_edges_from([
        [1,2,2], [ノード1, ノード2, 重み2]
        [2,3,5], [ノード2, ノード3, 重み5]
        [2,5,2], [ノード2, ノード5, 重み2]
        [3,4,1], [ノード3, ノード4, 重み1]
        [4,1,1], [ノード4, ノード1, 重み1]
    ])

	# グラフG上でノード1からノード5までの経路情報を取得
    path = nx.dijkstra_path(G, 1, 5)
	
	# グラフG上でノード1からノード5までの最短コストを取得
    length = nx.dijkstra_path_length(G, 1, 5)

	# 結果を出力
    print(path)
    print(length)

if __name__ == "__main__":
    shortest_path()
