# input jumlah 1 meter, 5 meter dan panjang
ubin1 = int(input('Masukkan jumlah ubin 1 meter: '))
ubin5 = int(input('Masukkan jumlah ubin 5 meter: '))
panjang = int(input('Masukkan panjang yang ingin ditutupi ubin: '))

# cek dulu panjang totalnya bisa apa nggak?
if (1 * ubin1 + 5 * ubin5) >= panjang:
    # berarti mungkin bisa
    # cek apakah cukup pakai ubin5
    if panjang % 5 == 0 and panjang//5 <= ubin5:
        print('Bisa')
    elif panjang % 5 <= ubin1:
        print('Bisa')
    else:
        print('Tidak bisa')
else:
    # tidak bisa karena tidak cukup
    print('Tidak bisa')
