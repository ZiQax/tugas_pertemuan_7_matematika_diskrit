# Mendefinnisikan fungssi di python

# Contoh mendefinisikan dfungsi yang mencetak psan selamat


def selamat():
    print("Selamat datang di tugas kombinatorial")
    

## Ini adalah contoh pemanggilan fungsi ynng ssudh di definisikan
    
selamat() ## jika tidk ada argumen spesifik di dalam fungsinya maka dalam tulis ()kosong saja

## Argumen fungsi terletak di dalam kurung setelah parameter
## Contoh pemanggilan fungsi dengan argumen

def evenOdd(x):
    if(x%2 == 0):
        return "Even"
    else:
        return "Odd"
    
print(evenOdd(4))
print(evenOdd(5))


## Jenis fungsi argumen ada dua jenis dalam python yaitu argumen default, posisi, dan argumen kata kunci
## 1. Argumen default

def fungsi(i, x=30):
    
 print("i = ", i)
 print("x = ", x)
 
fungsi(10)


## 2. Argumen kata kunci
def karyawan(nama, usia, posisi):
    print("Nama saya", nama)
    print("Usia saya", usia, "tahun")
    print("Posisi saya", posisi)
    
karyawan(nama="Andi", usia=20, posisi="Programmer")

## 3. Argumen Posisi

def pengguna(nama, alamat, usia):
    print("Nama saya", nama)
    print("Alamat saya di", alamat)
    print("Usia saya", usia, "tahun")
    
pengguna(nama="Andi", alamat="Jl. Raya", usia=20) 

## 4. Argument sewenang - wenang
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
      print(arg)
    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
       print(f"{key} == {value}")
# Function call with both types of arguments
myFun('Hey', 'Selamat Datang', first='di Kampus', mid='Megah', last='UPB')