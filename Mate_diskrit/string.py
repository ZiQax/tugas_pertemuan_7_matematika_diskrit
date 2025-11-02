print('============== kutipan tunggal dan ganda ===============')

s1 = 'GfG' # kutipan tunggal
s2 = "GfG" # kutipan ganda
print(s1 + '\n')
print(s2)

print('============== kutipan multibaris ===============')

s = """Saya sedang belajar
String Python di kampus UPB"""
print(s)
s = '''Saya'adalah
mahasiswa'''
print(s)

print('============== akses index ===============')
s = "universias pelita bangsa"
print(s[0]) # Karakter pertama
print(s[4]) # Karakter ke-5

print('============== akses index negatif ===============')
s = "universitas pelita bangsa"
print(s[-10]) # Karakter ke-3
print(s[-5]) # Karakter ke-5 dari akhir

print('============== slicing ===============')
s = "UniversitasPelitaBangsa"
print(s[1:4]) # karakter dari indeks 1 hingga 3
print(s[:3]) # dari awal hingga indeks 2
print(s[3:]) # dari indeks 3 hingga akhir
print(s[::-1]) # senar terbalik

print('============== Akses Indexing ===============')
s = "UniversitasPelitaBangsa"
print(s[1:4]) # karakter dari indeks 1 hingga 3
print(s[:3]) # dari awal hingga indeks 2
print(s[3:]) # dari indeks 3 hingga akhir
print(s[::-1]) # senar terbalik


print('============== looping ===============')
s = "TeknikIndustri"
for char in s:
 print(char)
 
print('============== operasi pada string ===============')
s = "universitaspelitabangsa"
s = "G" + s[1:] # Membuat string baru
print(s)

print('============== menghapus string ===============')
s = "UPB"
del s

print('============== pembaruan karakter ===============')
s = "halo pelitabangsa"
s1 = "H" + s[1:] # Perbarui karakter pertama
s2 = s.replace("pelita", "kekampus") # Ganti Word
print(s1)
print(s2)

print('============== operasi mengihitung panjang indeks ===============')
s = "universitaspelitabangsa"
print(len(s))

print("============== Uppercase dan Lowercase ===============")
s = "Hello World"
print(s.upper())
print(s.lower())


print("============== strip dan replace ===============")
s = " UPB "
print(s.strip())
s = "Python itu menyenangkan"
print(s.replace("menyenangkan", "Keren"))