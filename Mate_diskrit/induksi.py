def verify_basis_step(n):
    """Verifikasi langkah basis untuk n = 1"""
    return 2**n >= n + 1

def verify_inductive_step(k):
    """Verifikasi langkah induktif untuk n = k + 1"""
    # Asumsikan P(k) benar: 2^k ≥ k + 1
    # Buktikan P(k+1) benar: 2^(k+1) ≥ (k+1) + 1
    
    # Hitung kedua sisi untuk k+1
    left_side = 2**(k+1)  # 2^(k+1)
    right_side = (k+1) + 1  # (k+1) + 1
    
    return left_side >= right_side

def demonstrate_proof():
    print("Bukti Induksi Matematika: 2ⁿ ≥ n + 1 untuk semua n ≥ 1")
    print("=" * 60)
    
    # Langkah 1: Basis Step (n = 1)
    print("\n1. Langkah Basis (n = 1):")
    n = 1
    basis_result = verify_basis_step(n)
    print(f"   Untuk n = 1:")
    print(f"   2¹ = {2**n}")
    print(f"   1 + 1 = {n+1}")
    print(f"   2¹ ≥ 1 + 1 adalah {basis_result}")
    
    if not basis_result:
        print("   Bukti gagal pada langkah basis!")
        return
    
    # Langkah 2: Inductive Step
    print("\n2. Langkah Induktif:")
    print("   Asumsikan P(k) benar untuk suatu k ≥ 1")
    print("   yaitu: 2ᵏ ≥ k + 1")
    print("\n   Akan dibuktikan P(k+1) juga benar:")
    print("   yaitu: 2^(k+1) ≥ (k+1) + 1")
    
    # Demonstrasikan untuk beberapa nilai k
    print("\n   Verifikasi untuk beberapa nilai k:")
    for k in range(1, 5):
        inductive_result = verify_inductive_step(k)
        print(f"\n   Untuk k = {k}:")
        print(f"   2^({k}+1) = {2**(k+1)}")
        print(f"   ({k}+1) + 1 = {(k+1) + 1}")
        print(f"   2^({k}+1) ≥ ({k}+1) + 1 adalah {inductive_result}")
    
    # Penjelasan aljabar
    print("\n3. Bukti Aljabar untuk Langkah Induktif:")
    print("   2^(k+1) = 2 × 2ᵏ")
    print("   Karena 2ᵏ ≥ k + 1 (hipotesis induksi)")
    print("   Maka: 2^(k+1) = 2 × 2ᵏ ≥ 2(k + 1) = 2k + 2 > k + 2 = (k+1) + 1")
    
    print("\nKesimpulan:")
    print("1. Langkah basis terbukti benar untuk n = 1")
    print("2. Jika pernyataan benar untuk k, maka terbukti benar untuk k + 1")
    print("3. Oleh prinsip induksi matematika, pernyataan terbukti benar untuk semua n ≥ 1")

if __name__ == "__main__":
    demonstrate_proof()