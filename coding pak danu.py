# Deklarasi
a = int(input("masukan bilangan a: "))
b = int(input("masukan bilangan b: "))
c = int(input("masukan bilangan c: "))

# Deskriptif
if (a > b) and (a > b):
    terbesar = a
else:
    if b > c:
        terbesar = b
    else:
        terbesar = c

# output
print(f"bilangan terbesar adalah: {terbesar}")



 
jam_kerja = int(input("jam kerja: "))
tarif = int(input("tarif per jam: "))

gaji = jam_kerja * tarif

print(f"dibayar: {gaji}")

#ini komentar menggunakan tanda '#'nyang tidak dapat diesekusi 
#baris satu (1)
#baris dua (2)

'''
ini adalah komentar yang berisikan penjelasan lebih satu baru yaitu dengan mengunakan tanda petik satu ''
'''

"""
ini adalah contoh komentar mengunakan tanda kutip dua ""
"""
print("hello world") #output text/string 
#print('hello world')

#mengunakan sepesial karakter !@#$%^&*(),./'[]/ pad komentar

#mencetak nama anda
print("luffy")

#mencetak angka, nilai
print(12)
print("ini adalah nilai 12") #sebagai string

print(''' Praktikum algoritma dan pemrograman 1
          Nama     : Levi marino jaya p.
          Nim      : 12222420010
          Angkatan : 2024
          Prodi    : sains dat
          Fakultas sains dan teknologi pertanian.
          Universitas muhammadiyah semarang''')