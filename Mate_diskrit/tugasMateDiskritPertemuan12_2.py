import networkx as nx 
import matplotlib.pyplot as plt 
# ======================== 
# 1. Membuat Graf Berarah 
# ======================== 

DG = nx.DiGraph() 
edges = [("A", "B"), ("C", "A"), ("A", "D"), ("D", "A")] 
DG.add_edges_from(edges) 
# ======================== 
# 2. Menghitung In-degree & Out-degree 
# ======================== 
print("\nDerajat pada Graf Berarah:") 
for node in DG.nodes(): 
 indeg = DG.in_degree(node) 
outdeg = DG.out_degree(node) 
print(f"{node} → in-degree = {indeg}, out-degree = {outdeg}, total = {indeg + outdeg}") 
# ======================== 
# 3. Gambar Graf Berarah 
# ======================== 
plt.figure(figsize=(5,4)) 
pos = nx.spring_layout(DG, seed=42) 
nx.draw(DG, pos, with_labels=True, node_color='lightgreen', 
node_size=1500, font_size=12, arrows=True) 
plt.title("Graf Berarah (Directed Graph)") 
plt.show()  