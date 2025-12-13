import networkx as nx
import matplotlib.pyplot as plt 

# ========================
# 1. Membuat Graf Tak Berarah
# ========================
G = nx.Graph()
# Menambah simpul
G.add_nodes_from(["A", "B", "C", "D"])
# Menambah sisi
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
G.add_edges_from(edges)

# ========================
# 2. Menghitung Derajat Simpul
# ========================
print("Derajat tiap simpul:")
for node in G.nodes():
    print(f"deg({node}) = {G.degree(node)}")

# ========================
# 3. Menggambar Graf
# ========================
plt.figure(figsize=(5,4))
pos = nx.spring_layout(G, seed=42)  # posisi otomatis terkunci (agar gambar tidak berubah-ubah)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=1500, font_size=12)

# Opsional: Jika ingin label pada garis, edges harus punya atribut dulu.
# Baris di bawah ini tidak akan menampilkan teks jika edges tidak punya label.
nx.draw_networkx_edge_labels(G, pos)

plt.title("Graf Tak Berarah")
plt.show()