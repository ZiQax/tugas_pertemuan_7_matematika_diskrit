# ============================================================
# PROGRAM : Menghitung Peluang Kasus Sederhana
# MATA KULIAH : Matematika Diskrit
# LEVEL : TI.25.C3 / 312510158 / Angga Qomaruzzaman
# ============================================================
import itertools
# -----------------------------
# Fungsi dasar menghitung peluang
# -----------------------------
def peluang(kejadian, ruang_sampel):
 """
 Menghitung peluang sederhana:
 P(A) = jumlah kejadian / jumlah ruang sampel
 """
 return len(kejadian) / len(ruang_sampel)
# -----------------------------
# 1. Peluang melempar dadu
# -----------------------------
def peluang_dadu(angka):
 ruang_sampel = [1, 2, 3, 4, 5, 6]
 kejadian = [x for x in ruang_sampel if x == angka]
 return peluang(kejadian, ruang_sampel)
# -----------------------------
# 2. Peluang melempar 1 koin
# -----------------------------
def peluang_koin(sisi):
 ruang_sampel = ["A", "G"] # 
 kejadian = [x for x in ruang_sampel if x == sisi]
 return peluang(kejadian, ruang_sampel)
# -----------------------------
# 3. Peluang dua koin muncul AA
# -----------------------------
def peluang_dua_koin_AA():
 ruang_sampel = list(itertools.product(["A", "G"], repeat=2))
 kejadian = [x for x in ruang_sampel if x == ("A", "A")]
 return peluang(kejadian, ruang_sampel)
# -----------------------------
# 4. Peluang dua angka (1–5) berjumlah 7
# -----------------------------
def peluang_jumlah_7():
 angka = [1, 2, 3, 4, 5]
 ruang_sampel = list(itertools.combinations(angka, 2))
 kejadian = [pair for pair in ruang_sampel if sum(pair) == 7]
 return peluang(kejadian, ruang_sampel)
# ----------------------------------------------------
# PROGRAM UTAMA
# ----------------------------------------------------
print("==============================================")
print(" PROGRAM PELUANG KASUS SEDERHANA")
print("==============================================")
print("\n1. Peluang angka 4 saat melempar dadu:")
print(" Hasil =", peluang_dadu(4))
print("\n2. Peluang muncul Angka (A) saat melempar koin:")
print(" Hasil =", peluang_koin("A"))
print("\n3. Peluang dua koin muncul AA:")
print(" Hasil =", peluang_dua_koin_AA())
print("\n4. Peluang jumlah 7 dari dua angka (1–5):")
print(" Hasil =", peluang_jumlah_7())
print("\nProgram selesai.")