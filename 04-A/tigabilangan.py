def cek_digit_kanan(bil1, bil2, bil3):
    # hitung digit paling kanan => dengan modulo 10
    digit_kanan1 = bil1 % 10
    digit_kanan2 = bil2 % 10
    digit_kanan3 = bil3 % 10
    # bandingkan apakah sama
    if digit_kanan1 == digit_kanan2 and digit_kanan2 == digit_kanan3:
        print('Semua digit paling kanannya sama')
    else:
        print('Tidak semuanya sama')


# input tiga bilangan
bil1 = int(input('Masukkan bilangan pertama: '))
bil2 = int(input('Masukkan bilangan kedua: '))
bil3 = int(input('Masukkan bilangan ketiga: '))
cek_digit_kanan(bil1, bil2, bil3)
