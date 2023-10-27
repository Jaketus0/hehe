# #range:meregenerate bilangan
# for i in range(1, 11, 2):
#     print(i)
# # bilangan 3 yang kurang dari 100
# for i in range(3, 100, 3):
#     print(i)
# #kelipatan 50 dari 1500 sampai 20000
# for i in range(1500, 20001, 50): #agar 20000 ikut maka ditambah 1
#     print(i)

# for i in range(15, 0, -1):#dari 15 sampai 1, pakai minus karena turun
#     print(i)

# #dari 15 sampai satu, dengan keterangan ganjil genap
# for i in range(1, 0, 16):
#     print(i)
#     if i % 2 == 0:
#         print(f'{i} Genap')
#     else:   
#         print(f'{i} Ganjil')

# #deret fibo
# def fibo(batas):
#     bil1 = 1
#     bil2 = 1
#     #tampilkan dua suku fibonacci pertama
#     if bil1 < batas:
#         print(bil1, end='\t')
#         print(bil2, end='\t')
#     #suku berikutnya dari bil1 + bil2
#     suku_baru = bil1 + bil2
#     while suku_baru < batas:
#         print(suku_baru, end='\t')
#         #geser bil1 dan bil2
#         bil1 = bil2
#         bil2 = suku_baru
#         #hitung lagi suku berikutnya
#         suku_baru = bil1 + bil2
# #program utama
# batas = int(input('Masukkan batas dari deret fibonacci: '))
# fibo(batas)

# #mencari bilangan prima
# import math
# def is_prime(number):
#     pembagi = 0
#     for i in range(1, int(math.sqrt(number+1))): #pencaharaian hanya sampai akar n
#         if number % i == 0:
#             pembagi += 1 # pembagi = pembagi + 1
#     if pembagi == 2:
#         return True
#     else :
#         return False
    
# #program utama
# number = int(input('Masukkan bilangan : '))
# hasil = is_prime(number)
# if hasil:
#     print('Bilangan Prima')
# else:
#     print('Bukan Prima')
# #user memasukkan batas
# def is_prime(number):
#     pembagi = 0
#     for i in range(1, number+1):
#         if number % i == 0:
#             pembagi += 1 # pembagi = pembagi + 1
#     if pembagi == 2:
#         return True
#     else :
#         return False
# bawah = int(input('bawah: '))
# atas = int(input('atas : '))
# for i in range(bawah, atas+1):
#     hasil = is_prime(i)
#     if hasil: 
#         print(i)

# #program tebak angka
# import random
# def generate_angka(bawah, atas):
#     angka_komputer = random.randrange(bawah, atas)
#     return angka_komputer
# #program utama
# #input level
# level = int(input('Masukkan level 1/2/3: '))
# if level == 1 : #easy
#     print('Level Easy [0...100]')
#     angka_komputer = generate_angka(0,100)
#     langkah = 6
# elif level == 2: #intermediate
#     print('Level Intermediate [0...1000]')
#     angka_komputer= generate_angka(0, 1000)
#     langkah = 10
# elif level == 3: 
#     print('Level Hard [0...1_000_000]')
#     angka_komputer = generate_angka(0, 1_000_000)
#     langkah = 12
# hasil = False #kalah
# tebakan = False
# while tebakan == False : #selama tebakan False, ulangi terus
#     if langkah == 0: 
#         break
#     tebakan_user = int(input(f'Masukkan tebakan anda:  '))
#     langkah = langkah - 1
#     if tebakan_user == angka_komputer:
#         tebakan = True
#         hasil = True
#         break
#     else :
#         if tebakan_user > angka_komputer:
#             print('Tebakan anda terlalu besar')
#         else :
#             print('Tebakan anda terlalu kecil')
#         print('Tebakan anda masih salah....')
# if hasil == True:
#     print(f'Selamat, anda menang. Tebakan anda benar. Sisa : {langkah}')
# else :
#     print('Anda sudah kehabisan langkah')

# angka_1 = input('Angka 1 : ')
# angka_2 = input('Angka 2 : ')
# a1 = angka_1[0]
# a2 = angka_1[1]
# b1 = angka_2[0]
# b2 = angka_2[1]
# sama = (a1==b1) or (a1==b2) or (b2==a1) or (b2==b2) 
# if sama:
#     print('Sama')
# else:
#     print('Tidak Sama')

# nama1 = input('Masukan nama : ')
# nama2 = input('Masukan nama : ')
# nama3 = input('Masukan nama : ')
# p1 = len(nama1)
# p2 = len(nama2)
# p3 = len(nama3)
# if p1 >= p2 and p1 >= p3:
#     print(f'{nama1} Lebih panjang')
# elif p2 >= p1 and p2 >= p3:
#     print(f'{nama2} Lebih panjang')
# else:
#     print(f'{nama3} lebih panjang')

# #mencari n hari
# def n_hari_berikutnya(nama, n): #senin, selasa, rabu, kamis, jumat, sabtu, minggu
#     n = n % 7
#     '''
#     senin = 0 
#     selasa = 1
#     rabu = 2
#     kamis = 3
#     jumat = 4
#     sabtu = 5
#     minggu = 6
#     '''
#     bobot = 0
#     if nama == 'selasa' :
#         bobot = 1
#     elif nama == 'rabu':
#         bobot = 2
#     elif nama == 'kamis':
#         bobot = 3
#     elif nama == 'jumat':
#         bobot = 4
#     elif nama == 'sabtu' :
#         bobot = 5
#     elif nama == 'minggu' :
#         bobot = 6
#     total = (bobot + n) % 7
#     if total == 0 :
#         print('senin')
#     elif total == 1:
#         print('selasa')
#     elif total == 2 : 
#         print('rabu')
#     elif total == 3 :
#         print('kamis')
#     elif total == 4 : 
#         print('jumat')
#     elif total == 5 :
#         print('sabtu')
#     elif total == 6 : 
#         print('minggu')
# nama = input('masukkan nama : ')
# n = int(input('Masukkan berapa hari kemudian : '))
# n_hari_berikutnya(nama,n)

# #contoh soal def : 
# def seleksi_kkn(sks):
#     #return True : Jika bisa ambil kkn, sks >= 110
#     #return Flase : Jika sks < 110
#     if sks >= 110:
#         return True
#     else : 
#         return False
# #program utama
# #input program yang sudah diambil
# sks = int(input('Masukkan jumlah sks yang sudah ditempuh : '))
# #proses seleksi
# hasil_seleksi = seleksi_kkn(sks)
# #output
# if hasil_seleksi == True :
#     print('Boleh mengambil KKN')
# else : 
#     print('Tidak boleh mangambi KKN')

# #menentukan nilai tertinggi kedua 
# def runner_up(a, b, c, d, e):
#     data = [a,b,c,d,e]
#     data.sort()
#     return data[1]
# print(runner_up(9.76, 9.9, 10.0,9.62,9.78))

# #6.3
# tinggi= int(input('tinggi: '))
# lebar= int(input('lebar: '))
# luas= tinggi*lebar
# angka= 0 
# while angka != luas: 
#     for i in range(lebar): 
#         angka+=1
#         print(angka,end=' ')
#     print()

#kalau mau pake index harus ada "in" dlu

# list_buah = ['Jeruk', 'Naga', 'Pepaya', 'Mangga']
# print(list_buah)
# # tambah data di belakang list
# list_buah.append('Sirsak')
# print(list_buah)
# # tambah data di awal list
# list_buah.insert(0, 'Jambu')
# print(list_buah)
# del list_buah[0:2]
# print(list_buah)

# a = "Hello, World!"
# print(a.replace("H", "J"))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price)) 

# alamat= 'jl pasundan' 
# print(' 🦖 '.join(alamat.split()))

# kalimat= input('Masukkan kalimat: ')
# print(kalimat.replace('a', 'i'))
#print(kalimat.replace('a', ''))

# my_list = ['apple', 'banana', 'orange', 'mango']
# sorted_list = sorted(my_list, key=len)
# print(sorted_list)

# tinggi = int(input("Masukkan tinggi jajargenjang: "))
# #ke arah kiri 
# for i in range(tinggi):
#     # Menggambar spasi pada setiap baris untuk membuat pola jajargenjang
#     for j in range(tinggi - i - 1):
#         print(" ", end="")
#     # Menggambar karakter "#" pada setiap baris
#     for j in range(tinggi):
#         print("#", end="")
#     print() # Pindah ke baris selanjutnya
# #ke arah kanan 
# for i in range(tinggi):
#     # Menggambar spasi pada setiap baris untuk membuat pola jajargenjang ke arah kiri
#     for j in range(i):
#         print(" ", end="")
    
#     # Menggambar karakter "#" pada setiap baris
#     for j in range(tinggi):
#         print("#", end="")    
#     print() # Pindah ke baris selanjutnya

# def cari_nilai(n):
#     nilai_max= max(list_angka)
#     nilai_min= min(list_angka)
# list_angka = []
# start=1
# n = int(input("Masukkan berapa nilai yang diinginkan: "))
# for i in range(n):
#     angka = int(input("Masukkan angka ke-{start}: "))
#     start+=1
#     list_angka.append(angka)

# nilai_max, nilai_min = cari_nilai(list_angka)
# print("Nilai maksimum dalam list adalah", nilai_max)
# print("Nilai minimum dalam list adalah",nilai_min)

##mengganti elemen lain dalam tuple 
# t=('a','b','c','d','e')
# t = ('A',) + t[1:]
# print(t)

# def inisial(daftar): 
#     jenis= dict()
#     for i in daftar: 
#         if i[0] in jenis.keys(): 
#             jenis[i[0]] += 1 
#             print(i, jenis[i[0]], sep='')
#         else: 
#             jenis[i[0]]= 1 
#             print(i)

# def hapus(data,angka): 
#     listtuple= list(data)
#     if angka in listtuple: 
#         listtuple.remove(angka)
#         data= tuple(listtuple)
#         print(data)

# def hitung(dompet):
#     total = 0
#     lembar = {}
#     for uang in dompet:
#         if uang in lembar:
#             lembar[uang] += 1
#         else:
#             lembar[uang] = 1
#         nominal = int(uang[4:])  # Mengambil nilai nominal uang
#         total += nominal
#     for uang, jumlah in lembar.items():
#         print(f"{jumlah} lembar senilai {uang}")
#     print(total)
# dompet = (
# "Rp. 100000","Rp. 20000",
# "Rp. 50000","Rp. 50000",
# "Rp. 10000","Rp. 5000")
# hitung(dompet)

# def bosan(daftar):
#     indeks = -1  # Indeks awal
#     hasil = ""
#     for nama in daftar:
#         try:
#             karakter = nama[indeks]
#             hasil += karakter
#         except IndexError:
#             hasil += "x"
#         indeks -= 1
#     print(hasil)
# # Contoh penggunaan fungsi
# daftar = ("Yusta", "Monic", "claresta", "Elisabeth", "Agustin", "Anastasya", "Wijaya")
# bosan(daftar)

# def hitungHonorAsisten(data, besaranHonor): 
#     result= {}
#     for matkul in data: 
#         for asdos in data[matkul]: 
#             if asdos not in result: 
#                 result[asdos]= besaranHonor
#             else: 
#                 result[asdos]+= besaranHonor
#     result= {k: v for k,v in sorted (result.items(), key= lambda item: item[0])}
#     return result
# data = {
#     'Alpro_A':['Rizky', 'Yusak', 'Shalom', 'Tania'],
#     'Alpro_B':['Dedi', 'Karen', 'Yusak', 'Tania'],
#     'Alpro_C':['Richard', 'Rizky', 'Mikael', 'Yusak'],
#     'Alpro_D':['Michelle', 'Tania','Dedi','Karen'],
#     'Jarkom_A':['Rizky', 'Vero'],
#     'Jarkom_B':['Riel','Natanael'],
#     'Jarkom_C':['Yulius','Kevin']
# }
# print(hitungHonorAsisten(data,45000))

# def cekKarakter(kalimat):
#     huruf= set('abcdefghijklmnopqrstuvwxyz')
#     baris_kalimat= set(kalimat)
#     if huruf - baris_kalimat: 
#         print('Kalimat tersebut tidak memiliki semua huruf') 
#     else: 
#         print('Kalimat tersebut memiliki semua huruf')
# kalimat = 'the quick brown fox jumps over the lazy cat'
# cekKarakter(kalimat)

# def daftar_tidak_sama(angka1,angka2,batas): 
#     daftar1= set(range(angka1, batas, angka1))
#     daftar2= set(range(angka2,batas,angka2))
#     daftartidaksama= daftar1.symmetric_difference(daftar2)
#     jumlah= len(daftartidaksama)
#     print(jumlah)
# daftar_tidak_sama(7,3,30)

# from math import sqrt
# def euclidienCalculation(dict1, dict2):
#     gabungan = set(dict1.keys()).union(set(dict2.keys()))
#     irisan = set(dict1.keys()).intersection(set(dict2.keys()))
#     M = len(gabungan)
#     N = len(irisan) 
#     sum_of_squared_diff = 0
#     for key in irisan:
#         diff = dict1[key] - dict2[key]
#         sum_of_squared_diff += diff ** 2
#     euclidean_relative = sqrt(sum_of_squared_diff) / M
#     return euclidean_relative
# o1 = {'a': 0.1724, 'b': 0.648, 'c': 0.021}
# o2 = {'a': 0.214, 'b': 0.048, 'd': 0.121}
# result = euclidienCalculation(o1, o2)
# print('EucRel: %0.3f' % result)
# o1 = {'a':0.5,'b':0.28,'c':0.821}
# o2 = {'a':0.214,'c':0.048,'e':0.121}
# print('EucRel: %0.3f'%euclidienCalculation(o1,o2))

# print('1. list menjadi set\n2. set menjadi list\n3. tuple menjadi set\n4. set menjadi tuple')
# pilihan = int(input('Masukkan pilihan: '))
# jumlah = int(input('Masukkan jumlah nilai yang ingin diinput: '))
# list_nilai = []
# for i in range(1, jumlah+1):
#     nilai=int(input(f'Nilai {i}: '))
#     list_nilai.append(nilai)
# if pilihan == 1:
#     print('List :')
#     print(list_nilai)
#     print('Set :')
#     print(set(list_nilai))
# elif pilihan == 2:
#     set_nilai = set(list_nilai)
#     print('Set :')
#     print(set_nilai)
#     print('List :')
#     print(list(set_nilai))
# elif pilihan == 3:
#     tuple_nilai = tuple(list_nilai)
#     print('Tuple :')
#     print(tuple_nilai)
#     print('Set :')
#     print(set(tuple_nilai))
# elif pilihan == 4:
#     set_nilai = set(list_nilai)
#     print('Set :')
#     print(set_nilai)
#     print('Tuple :')
#     print(tuple(set_nilai))
# else:
#     print('Eror')

# def seq(daftar,item): 
#     pos =0 
#     ketemu= False
#     while pos < len(daftar) and not ketemu: 
#         if daftar[pos] == item: 
#             ketemu= True
#         else: 
#             pos = pos+1
#         return ketemu, pos
# print(seq([11,23,58,31,56,77,43,12,65,19],11))

# def seq(daftar,item): 
#     pos = 0 
#     ketemu = False
#     while pos < len(daftar) and not ketemu: 
#         if daftar[pos] == item: 
#             ketemu= True
#         else: 
#             pos= pos+1
#     return ketemu, pos
# print(seq([11,23,58,31,56,77,43,12,65,19],40))

#utk membalikkan kata/kalimat
# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = numbers[::-1]
# print(reversed_numbers)  # Output: [5, 4, 3, 2, 1]

# #soal 1 
# a = int(input('Masukkan jumlah yang mau diinput: '))
# list1 =[]
# list2 =[]
# d = []
# for b in range(1,a+1): 
#     c = int(input(f'Masukkan nilai {b} list ke 1 : '))
#     list1.append(c)
# for b in range(1,a+1): 
#     c = int(input(f'Masukkan nilai {b} list ke 2 : '))
#     list1.append(c)
# gabung = list1 + list2 
# gabung.sort()
# d.append(gabung)
# print(d)

# #soal 2 
# dictionary = {'A':100,'B':540,'C':239, 'D':250,'E':265,'F':360, 'G':450}
# total = 0
# for i in dictionary.values(): 
#     total+=i
# print(f"Total = {total}")

# #hitung rata rata 
# n=int(input("Masukan jumlah elemen yang akan diinputkan: "))
# a=[]
# for i in range(0,n):
#     elem=int(input("Masukan element: "))
#     a.append(elem)
# avg=sum(a)/n
# print("Rata-rata elements pada list adalah ",round(avg,2))

# organisasi = {
#     'koperasi':{
#         'nama':'Koperasi Tani Modern',
#         'berdiri': 1987,
#         'kepala':'bambang',
#         'cabang': ['Jakarta','Surabaya','Denpasar']
#     },
#     'pemuda desa': {
#         'nama': 'Paguyuban Pemuda Desa ',
#         'berdiri':2001,
#         'kepala': 'joni',
#         'cabang': ['desa Topan','desa badai']
#     }
# }
# print(organisasi['pemuda desa']['berdiri'])

# fruits = open('fruits.txt', 'w')
# fruits.write('Apple\n')
# fruits.write('Mango\n')
# fruits.write('Orange\n')
# fruits.write('Banana\n')
# fruits.close()
# fruits = open('fruits.txt', 'r')
# fruit_list = fruits.readlines()
# print('Fruit count: ', len(fruit_list))
# print(fruit_list)
# for fruit in fruit_list:
#     print(fruit.strip())
# fruits.close()

# class Mahasiswa: 
#     _nim = ""
#     _nama = ""
#     _ipk = 0.0
# m = Mahasiswa
# m._nim = "1"
# m._nama = "van"
# print(m._nim, m._nama)

# class KartuKredit: 
#     def __init__(self,noKartu,namaPengguna,limit,saldo):
#         self._nokartu = noKartu
#         self._namapengguna = namaPengguna
#         self._limit = limit
#         self._saldo = saldo 
#     def setNoKartu(self, noKartu):
#         self._nokartu = noKartu
#         # return True     
#     def getNoKartu(self): 
#         return self._nokartu
#     def setNamaPengguna(self, namaPengguna): 
#         self._namapengguna = namaPengguna
#     def getNamaPengguna(self): 
#         return self._namapengguna
# k1 = KartuKredit("1","Anton",10000,500)
# print(k1.getNamaPengguna())

# #nama file: lingkaran hehe 
# import math
# class Lingkaran: 
#     def __init__(self,jari2): 
#         self.jari2 = jari2 
#     def hitungLuas(self): 
#         return math .pi * self.jari2**2
#     def hitungKeliling(self): 
#         return math.pi*2*self.jari2
# #buat file baru nama misal "main"
# from lingkaran hehe import Lingkaran 
# l = Lingkaran(7)
# print("Luas: "+str(l.hitungLuas()))
# print("Keliling: "+str(l.hitungKeliling()))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)