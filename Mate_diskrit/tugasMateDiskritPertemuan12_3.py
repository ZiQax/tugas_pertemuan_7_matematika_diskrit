import networkx as nx 
# MultiGraph = graf yang boleh punya sisi ganda dan loop 
MG = nx.MultiGraph() 
# Tambahkan sisi termasuk loop 
MG.add_edge("A", "B") 
MG.add_edge("A", "B")   # sisi ganda 
MG.add_edge("A", "A")   # loop 
# Hitung derajat secara manual untuk memperlihatkan aturan loop = 2 derajat 
print("\nDerajat pada Multigraph (loop dihitung 2):") 
for node in MG.nodes(): 
 print(f"deg({node}) = {MG.degree(node)}") 
