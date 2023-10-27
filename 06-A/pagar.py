def pagar_vertikal(n):
    print('Pagar Vertikal')
    for i in range(n):
        print('#')
    print()  # beri jarak untuk output berikutnya


def pagar_horizontal(n):
    print('Pagar Horizontal')
    for i in range(1, n+1):
        print('#', end='')
    print()  # beri jarak untuk output berikutnya


def persegi(n):
    print('Pagar Persegi')
    for baris in range(1, n+1):
        for kolom in range(n):
            print('#', end='')
        print()
    print()  # beri jarak untuk output berikutnya


def persegi_bolong(n):
    print('Persegi Bolong')
    for baris in range(1, n+1):
        if baris == 1 or baris == n:
            for kolom in range(n):
                print('#', end='')
        else:
            spasi = n - 2
            print('#', end='')
            for i in range(spasi):
                print(' ', end='')
            print('#', end='')
        print()
    print()  # beri jarak untuk output berikutnya


def huruf_x(n):
    print('Pagar Huruf X')
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if baris == kolom:
                print('#', end='')
            elif baris+kolom == n+1:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()  # beri jarak untuk output berikutnya


def huruf_z(n):
    print('Pagar huruf Z')
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            # print penuh untuk baris 1 dan terakhir
            if baris == 1 or baris == n:
                print('#', end='')
            elif baris+kolom == n+1:
                print('#', end='')
            else:
                print(' ', end='')
        print()  # ganti baris
    print()  # beri jarak untuk output berikutnya


def huruf_n(n):
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if kolom == 1 or kolom == n:
                print('#', end='')
            elif baris == kolom:
                print('#', end='')
            else:
                print(' ', end='')
        print()  # ganti baris
    print()  # jarak ke output berikutnya (opsional)


def plus(n):
    tengah = 1 + (n // 2)
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if baris == tengah or kolom == tengah:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()


def segitiga_kiri(n):
    for baris in range(1, n+1):
        for kolom in range(1, baris+1):
            print('#', end='')
        print()  # ganti baris
    print()  # jarak ke output berikutnya


def segitiga_kanan(n):
    for baris in range(1, n+1):
        # hitung berapa pagar yang harus muncul
        pagar = baris
        # hitung berapa spasi yang harus muncul
        spasi = n - pagar
        # print spasi dulu
        for kolom in range(spasi):
            print(' ', end='')
        # print pagar
        for kolom in range(pagar):
            print('#', end='')
        print()  # ganti baris
    print()  # untuk output berikutnya (opsional)


def segitiga_tengah(n):
    for baris in range(1, n+1):
        spasi = n - baris
        pagar = 2 * baris - 1
        # print spasi
        for i in range(spasi):
            print(' ', end='')
        # print pagar
        for i in range(pagar):
            print('#', end='')

        print()  # ganti baris
    print()  # jarak ke output berikutnya


def zigzag(n):
    print('Zig zag')
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if baris % 2 == 1:
                # print pagar satu baris full
                print('#', end='')
            elif baris % 4 == 0:
                print('#', end='')
                break
            else:
                # print spasi (n-1) + pagar 1x
                if kolom == n:
                    print('#', end='')
                else:
                    print(' ', end='')
        print()
    print()

    # program utama
n = int(input('Masukkan n: '))
pagar_vertikal(n)
pagar_horizontal(n)
persegi(n)
persegi_bolong(n)
huruf_x(n)
huruf_z(n)
huruf_n(n)
plus(n)
segitiga_kiri(n)
segitiga_kanan(n)
segitiga_tengah(n)
zigzag(n)
