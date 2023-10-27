# # angka = input("Masukkan angka pecahan: ")
# # if ('.' or ',') in angka: 
# #     print(angka.split(".",1)[1])
# # else:
# #     print("Bilangan bulat")

# # angka = input("masukkan angka: ")
# # tipe = type(angka)
# # print(tipe)

# switcher={
#     0="satu",
#     1="dua",
#     2="tiga",
# }
# print(switcher.get(2,"kosong"))

# nama=st(input("Masukkan Nama: "))
# if nama=="Bond":
#     print("Selamat Datang agen 007")
# else: 
#     print("Selamat Datang",nama)

# list=[2,4,232,324,423,546,565]
# list1=['a','b','c','d','e','f','g']
# list1.sort()
# print("Dari yang paling awal adalah",list1)
# list1.sort(reverse=True)
# print("Dari yang paling akhir adalah",list1)

# print("~~ Selamat Datang di Program Pengurutan Bilangan ~~")
# print("Tentukan Pilihan Anda!!! [1/2]")
# print("1. Ascending") #dri kecil
# print("2. Descending") #dri besar 
# print("3. Mean") #rata-rata
# print()
# pil= int(input("Masukkan pilihan yang anda inginkan: "))
# if pil>10:
#     print("inputan salah")
#     exit()
# bil1= int(input("Masukkan bilangan pertama: "))
# bil2= int(input("Masukkan bilangan kedua: "))
# bil3= int(input("Masukkan bilangan ketiga: "))
# bil4= int(input("Masukkan bilangan keempat: "))
# bil5= int(input("Masukkan bilangan kelima: "))
# bil6= int(input("Masukkan bilangan keenam: "))
# if pil==1:
#     list=[bil1,bil2,bil3,bil4,bil5,bil6]
#     list.sort()
#     print("Urutan bilangan dari yang terkecil adalah",list)
# elif pil==2:
#     list=[bil1,bil2,bil3,bil4,bil5,bil6]
#     list.sort(reverse=True)
#     print("Urutan bilangan dari yang terbesar adalah",list)
# elif pil==3: 
#     list=[bil1,bil2,bil3,bil4,bil5,bil6]
    
# def imy():
#     print("paniot");
# imy()

# def luas():
#     luas=alas*tinggi/2
#     print("Luas segitiga= ",luas)
#     return luas 
# alas=int(input("Masukkan alas= "))
# tinggi=int(input("Masukkan tinggi= "))
# luas()

# def suhu():
#     r= 4/5*c
#     print("Hasil Konversi suhu",c,"adalah",r,"Reamur")
#     f= 9/5*c+32
#     print("Hasil Konversi suhu",c,"adalah",f,"Farenheit")
#     k= c+273
#     print("Hasil Konversi suhu",c,"adalah",k,"Kelvin")
#     return suhu
# c=int(input("Masukkan skala celcius: "))
# suhu()

# def conv_reamur(celcius):
#     convert_reamur = 4 / 5 * celcius
#     return convert_reamur
# def conv_farenheit(celcius):
#     convert_farenheit = 9 / 5 * celcius  + 32
#     return convert_farenheit
# def conv_kelvin(celcius):
#     convert_kelvin = celcius + 273
#     return convert_kelvin
# print('++++++++++ PROGAM KONVERSI SUHU ++++++++++ \n')
# temperature = int(input('Masukan Skala Celcius: '))
# reamur = conv_reamur(temperature)
# farenheit = conv_farenheit(temperature)
# kelvin = conv_kelvin(temperature)
# print("\nHasil Konversi Suhu ", temperature, "C adalah ",reamur, "Reamur")
# print("Hasil Konversi Suhu ", temperature, "C adalah ",farenheit, "Farenheit")
# print("Hasil Konversi Suhu ", temperature, "C adalah ",kelvin, "Kelvin")
# print('++++++++++++++++++++++++++++++++++++++++++++')

# for i in range(1, 11):
#     print('*'*i)

# angka= int(input("Masukkan angka: "))
# for i in range(angka):
#     print('  '*i,('* '*(angka-i)+('* '*(angka-(i+1)))))

# no 3
# a= int(input("masukkan angka: "))
# for i in range (0, a):
#     c=1
#     print(c, end=' ')
#     for j in range (a-i-1,0,-1):
#         print('*', end=' ')
#         c=c+1 
#         print(c, end=' ')
#     print('\n')

# import turtle
# s= turtle. Screen()
# t= turtle.Turtle()
# s.bgcolor
# t.forward(100)
# s.exitonclick()

# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)

#program mengecilkan kalimat/kata
# a= input("masukkan kata: ")
# b= a.casefold()
# print("hasil:" ,b)

#hitung ada brpa kata/kalimat di dlm input
# inpt= input("masukkan kata/kalimat: ")
# b= inpt.count("a")
# print("jumlah",inpt, "dalam kata/kalimat tersebut adalah",b)

# text= {'Lorem','Ipsum', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'typesetting', 'industry', 'Lorem', 'Ipsum' ,'has', 'been' ,'the', 'industry'}
# inpt= input("Search= ")
# if inpt in text:
#     print("#",inpt,"found!")
# else: 
#     print("not found!")

# #len() untuk hitung ad brp di list 
# text= {'Lorem','Ipsum', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'typesetting', 'industry', 'Lorem', 'Ipsum' ,'has', 'been' ,'the', 'industry'}
# print(text,'panjangnya adalah: ',len(text))

# price=3 
# print('harga apel '+str(price)+' dolar')

# paragraph = """Ini adalah paragraph. Paragraf
# terdiri dari beberapa baris"""
# print(paragraph)

# for i in range (1,6): 
#     print("*")

# #di folder yang sama 
# namafile= 'log.txt'
# # #windows 
# # namafile= 'D:\\Android\\data.txt'
# # #linux
# # namafile= '\var\www\data.txt'
# handle= open(namafile,'r') #r= mode membaca 
# # #mode= r ,w ,a , b->binary 
# for baris in handle: 
#     print(baris, end='')
#ngambil baris tertentu 
# no_baris= 1 
# n=3 
# for baris in handle: 
#     if no_baris==n: 
#         print(baris, end='') 
#     no_baris= no_baris+1 
# # handle.close() #wajib selalu dilakukan 
# print(namafile) 

# jlhinputan= int(input('Masukkan jumlah inputan: '))
# start= 1 
# listisi= []
# for i in range(jlhinputan):
#     isi= input('Masukkan isi: ')
#     listisi.append(isi)
# print(f'list: ')
# for i in range(jlhinputan): 
#     print(f'{start}. {listisi[i]}')
#     start+=1


# import calendar
# # Menghitung jumlah hari dalam bulan Februari pada tahun tertentu
# tahun = 2023  # Ganti dengan tahun yang diinginkan
# jumlah_hari = calendar.monthrange(tahun, 2)[1]
# print("Jumlah hari dalam bulan Februari tahun", tahun, "adalah", jumlah_hari)

# tahun = int(input("Masukkan tahun: "))  # Ganti dengan tahun yang diinginkan
# # Memeriksa apakah tahun merupakan tahun kabisat atau bukan
# if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
#     jumlah_hari = 29  # Jika tahun kabisat, Februari memiliki 29 hari
# else:
#     jumlah_hari = 28  # Jika bukan tahun kabisat, Februari memiliki 28 hari
# print("Jumlah hari dalam bulan Februari tahun", tahun, "adalah", jumlah_hari)

# #hitung faktorial 
# def hitung_faktorial(n):
#     total = 1
#     for i in range(1, n+1):
#         total *= i
#     return total

# result = hitung_faktorial(5)
# print(result)

