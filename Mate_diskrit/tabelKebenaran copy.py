def implikasi (p, q):
    """
    Menghitung hasil implikasi logika P → Q
    P → Q bernilai False hanya jika P True dan Q False
    """
    return (not p) or q
def cetak_tabel_kebenaran():
    """
    Mencetak tabel kebenaran untuk membuktikan (P → Q) ≡ (¬P ∨ Q)
    """
    print('\n Tabel Kebenaran untuk membuktikan (P → Q) ≡ (¬P ∨ Q)')
    print("=" * 60)
    print("| P | Q | ¬P | P → Q | ¬P ∨ Q | (P → Q) ≡ (¬P ∨ Q) |")
    print("-" * 60)
    # Menghasilkan semua kemungkinan kombinasi P dan Q
    
    for p in [True, False]:
        for q in [True, False]:
            # Menghitung ¬P
            not_p = not p
            
            # Menghitung P → Q
            implikasi_hasil = implikasi(p, q)
            
            # Menghitung ¬P ∨ Q
            or_hasil = not_p or q
            
            # Memeriksa apakah ekuivalen
            ekuivalen = implikasi_hasil == or_hasil
            
            # Mencetak baris tabel kebenaran
            print(f"| {int(p)} | {int(q)} |  {int(not_p)} |   {int(implikasi_hasil)}   |    {int(or_hasil)}   |         {str(ekuivalen)}        |")
    print("-" * 60)
    # Menambahkan penjelasan hasil
    print("\nPenjelasan:")
    print("1. P → Q    = Implikasi (jika P maka Q)")
    print("2. ¬P ∨ Q   = Or (salah satu P atau Q)")
    print("\nKesimpulan:")
    print("Dari tabel kebenaran di atas, dapat dilihat bahwa")
    print("(P → Q) ≡ (¬P ∨ Q) bernilai True jika dan hanya jika P bernilai False dan Q bernilai True.")
if __name__ == "__main__":
    cetak_tabel_kebenaran()
    
    