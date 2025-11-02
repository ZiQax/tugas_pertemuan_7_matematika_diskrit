print('=============== Simulasi Tabel Kebenaran ===============');

import itertools

# Definisi fungsi implikasi

def implies(p,q):
    return (not p) or q

# Header Tabel Kebenaran
print(f'{"p":<5}{"q":<5}{"p and q":<10}{"p or q":<10}{"-p":<5}{"p -> q":<8}')

# Iterasi semua kombinasi p dan q (True/False)

for p, q in itertools.product([True, False], repeat=2):
    print(f'{p!s:<5}{q!s:<5}{p and q!s:<10}{p or q!s:<10}{not p!s:<5}{implies(p,q)!s:<8}')

print('======================================================');   

print('=============== Pembuktian Tabel Kontradiksi Sederhana ===============');

def is_odd(n):
    return n % 2 == 1
def proof_by_contradiction(n):
    for n in range(1, 10):
        if is_odd(n**2) and not is_odd(n):
            print(f'Kontradiksi diteukan pada n = {n}!')
            return False
    print("tidak ada kontadiksi ditemukan --> pertanyataan benar (jika n ganjil maka n ganjil).")
    return True
proof_by_contradiction(n=2)

print('======================================================');   

# Uji Tautologi dengan Tabel Kebenaran

print('=============== Uji Tautologi dengan Tabel Kebenaran ===============');

def check_tautology():
    tautology = True
    for p, q in itertools.product([True, False], repeat=2):
        result = implies(p and q, p)
        print(f'p={p}, q={q}, (p ∧ q) -> p = {result}')
        if not result:
            tautology = False
        print("\nKesimpulan : ","TAUTOLOGY" if tautology else "BUKAN TAUTOLOGY") 
check_tautology()


print('======================================================');
                   