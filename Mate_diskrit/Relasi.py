from typing import Set, Tuple, List
Pair = Tuple[int, int] # tipe untuk pasangan terurut; bisa diganti ke generik jika mau

def to_set(pairs: List[Pair]) -> Set[Pair]:
	return set(pairs)

def is_reflexive(A: Set[int], R: Set[Pair]) -> bool:
	for a in A:
		if (a, a) not in R:
			return False
	return True

def is_symmetric(R: Set[Pair]) -> bool:
	for (a, b) in R:
		if (b, a) not in R:
			return False
	return True

def is_transitive(R: Set[Pair]) -> bool:
	# cek semua kombinasi (a,b), (b,c)
	for (a, b) in R:
		for (x, c) in R:
			# jika pasangan kedua berawal dari b, artinya x == b
			if x == b:
				if (a, c) not in R:
					return False
	return True

def relation_matrix(A_sorted: List[int], R: Set[Pair]) -> List[List[int]]:
	"""Buat matriks biner representasi relasi. A_sorted harus urutan elemen A yang konsisten."""
	idx = {a: i for i, a in enumerate(A_sorted)}
	n = len(A_sorted)
	M = [[0]*n for _ in range(n)]
	for (a, b) in R:
		if a in idx and b in idx:
			M[idx[a]][idx[b]] = 1
	return M

def print_matrix(A_sorted: List[int], M: List[List[int]]):
	"""Cetak matriks relasi dengan label baris/kolom."""
	header = " " + " ".join(f"{x:>3}" for x in A_sorted)
	print(header)
	for i, row in enumerate(M):
		print(f"{A_sorted[i]:>3} " + " ".join(f"{val:>3}" for val in row))

def is_equivalence(A: Set[int], R: Set[Pair]) -> bool:
	"""Relasi ekuivalen bila refleksif, simetris, dan transitif."""
	return is_reflexive(A, R) and is_symmetric(R) and is_transitive(R)

# --------------------
# Contoh penggunaan
# --------------------
if __name__ == "__main__":
	# Contoh 1
	A1 = {1, 2, 3}
	R1 = to_set([(1,1), (2,2), (3,3), (1,2), (2,1)])
	print("Contoh 1")
	print("A =", A1)
	print("R =", sorted(R1))
	print("Refleksif:", is_reflexive(A1, R1))
	print("Simetris :", is_symmetric(R1))
	print("Transitif:", is_transitive(R1))
	print("Ekuivalen:", is_equivalence(A1, R1))
	print()
	# Tampilkan matriks relasi
	A_sorted = sorted(A1)
	M1 = relation_matrix(A_sorted, R1)
	print("Matriks relasi (baris->a, kolom->b):")
	print_matrix(A_sorted, M1)
	print("\n" + "-"*40 + "\n")
	
	# Contoh 2: non-transitif
	A2 = {1,2,3}
	R2 = to_set([(1,1), (2,2), (3,3), (1,2), (2,3)]) # tidak ada (1,3)
	print("Contoh 2")
	print("A =", A2)
	print("R =", sorted(R2))
	print("Refleksif:", is_reflexive(A2, R2))
	print("Simetris :", is_symmetric(R2))
	print("Transitif:", is_transitive(R2))
	print("Ekuivalen:", is_equivalence(A2, R2))
	print()
	M2 = relation_matrix(sorted(A2), R2)
	print("Matriks relasi:")
	print_matrix(sorted(A2), M2)
	print("\n" + "-"*40 + "\n")
	
	# Contoh 3: simetris tapi tidak refleksif
	A3 = {1,2}
	R3 = to_set([(1,2), (2,1)]) # simetris, tapi (1,1) dan (2,2) tidak ada
	print("Contoh 3")
	print("A =", A3)
	print("R =", sorted(R3))
	print("Refleksif:", is_reflexive(A3, R3))
	print("Simetris :", is_symmetric(R3))
	print("Transitif:", is_transitive(R3))
	print("Ekuivalen:", is_equivalence(A3, R3))
	print()
	M3 = relation_matrix(sorted(A3), R3)
	print("Matriks relasi:")
	print_matrix(sorted(A3), M3)
	print("\n" + "-"*40 + "\n")

	# Contoh tambahan: fungsi untuk mencari penutupan transitif (opsional)
	def transitive_closure(R: Set[Pair]) -> Set[Pair]:
		closure = set(R)
		added = True
		while added:
			added = False
			new_pairs = set()
			for (a,b) in closure:
				for (x,c) in closure:
					if x == b and (a,c) not in closure:
						new_pairs.add((a,c))
			if new_pairs:
				closure |= new_pairs
				added = True
		return closure

	print("Penutupan transitif R2:", sorted(transitive_closure(R2)))