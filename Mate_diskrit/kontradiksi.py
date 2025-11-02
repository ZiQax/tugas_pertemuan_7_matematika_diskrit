def bukti_kontradiksi():
    print("Bukti Kontradiksi: 'Tidak ada bilangan bulat ganjil yang habis dibagi 2'")
    print("=" * 70)
    
    # Langkah 1: Asumsikan negasi dari pernyataan
    print("1. Asumsikan pernyataan salah (negasi):")
    print("   'Ada bilangan bulat ganjil yang habis dibagi 2'")
    print()
    
    # Langkah 2: Misalkan ada bilangan seperti itu
    print("2. Misalkan n adalah bilangan bulat ganjil tersebut")
    print("   Karena n ganjil, maka n = 2k + 1, dimana k adalah suatu bilangan bulat")
    print()
    
    # Langkah 3: Karena dapat dibagi 2
    print("3. Karena n habis dibagi 2, maka:")
    print("   n = 2m, dimana m adalah suatu bilangan bulat")
    print()
    
    # Langkah 4: Tunjukkan kontradiksi
    print("4. Dari (2) dan (3), kita dapat tulis:")
    print("   2k + 1 = 2m")
    print("   1 = 2(m - k)")
    print("   1 = bilangan genap")
    print()
    
    # Langkah 5: Kesimpulan
    print("5. Kontradiksi!")
    print("   1 adalah bilangan ganjil, tidak mungkin sama dengan bilangan genap")
    print("   Oleh karena itu, asumsi kita salah")
    print()
    
    print("Kesimpulan:")
    print("Pernyataan awal benar: 'Tidak ada bilangan bulat ganjil yang habis dibagi 2'")

if __name__ == "__main__":
    bukti_kontradiksi()