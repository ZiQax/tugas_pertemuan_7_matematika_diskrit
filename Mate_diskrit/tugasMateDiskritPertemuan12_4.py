import networkx as nx 
import matplotlib.pyplot as plt 
def buat_graf_undirected(nodes, edges): 
 G = nx.Graph() 
 G.add_nodes_from(nodes) 
 G.add_edges_from(edges) 
 return G 
def hitung_derajat(G): 
 return {node: G.degree(node) for node in G.nodes()} 
def gambar_graf(G, title="Graf"): 
 pos = nx.spring_layout(G, seed=42) 
 nx.draw(G, pos, with_labels=True, node_color="lightblue", 
 node_size=1500) 
 plt.title(title) 
 plt.show() 
# Contoh penggunaan 
nodes = ["A", "B", "C", "D"] 
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")] 
G = buat_graf_undirected(nodes, edges) 
print(hitung_derajat(G)) 
gambar_graf(G, "Contoh Graf")