# input
nama1 = input('Masukkan nama 1: ')
nama2 = input('Masukkan nama 2: ')
nama3 = input('Masukkan nama 3: ')

# hitung panjangnya
panjang1 = len(nama1)
panjang2 = len(nama2)
panjang3 = len(nama3)

# tentukan siapa yang terpanjang
# jika nama1 yang terpanjang
if panjang1 >= panjang2 and panjang1 >= panjang3:
    print(nama1)
# jika nama2 yang terpanjang
elif panjang2 >= panjang1 and panjang2 >= panjang3:
    print(nama2)
# kalau tidak berarti nama3 yang paling panjang
else:
    print(nama3)
