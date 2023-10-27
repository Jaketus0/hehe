def pagar_vertikal(n):
    # tampilkan # sejumlah n secara vertikal
    for i in range(n):
        print('#')


def pagar_horizontal(n):
    # tampilkan # sejumlah n secara vertikal
    for i in range(n):
        print('#', end='')
    print()


def persegi(n):
    # print n baris
    for i in range(n):
        for j in range(n):
            print(i, end='')
        print()


def segitiga_kiri(n):
    for baris in range(1, n+1):
        for kolom in range(1, baris+1):
            print('#', end='')
        print()


def segitiga_kanan(n):
    for baris in range(1, n+1):
        spasi = n - baris
        pagar = baris
        # cetak spasi sebanyak spasi
        for kolom_spasi in range(spasi):
            print(' ', end='')
        for kolom_pagar in range(pagar):
            print('#', end='')
        print()  # ganti baris


def persegi_bolong(n):
    # print pagar full di baris pertama
    for kolom in range(n):
        print('#', end='')
    print()
    # print bagian bolong sebanyak n-2 baris
    for baris in range(n-2):
        spasi = n - 2
        print('#', end='')
        for kolom in range(spasi):
            print(' ', end='')
        print('#')
    # print pagar full untuk baris terakhir
    for kolom in range(n):
        print('#', end='')
    print()


def huruf_x(n):
    for baris in range(n):
        for kolom in range(n):
            if baris == kolom:    # diagonal ke kanan bawah
                print('#', end='')
            elif baris+kolom == n-1:  # diagonal ke kiri bawah
                print('#', end='')
            else:
                print(' ', end='')
        print()


def tanda_plus(n):
    for baris in range(n):
        for kolom in range(n):
            if baris == n//2:
                print('#', end='')
            elif kolom == n//2:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    # program utama


def karpet(n):
    # segitiga atas
    for baris in range(1, (n//2)+1):
        pagar = 2 * baris - 1
        spasi = (n - pagar)//2
        # print spasi
        for i in range(spasi):
            print(' ', end='')
        # print pagar
        for i in range(pagar):
            print('#', end='')
        print()
    # segitiga bawah
    for baris in range((n//2)-1, 0, -1):
        pagar = 2 * baris - 1
        spasi = (n - pagar)//2
        # print spasi
        for i in range(spasi):
            print(' ', end='')
        # print pagar
        for i in range(pagar):
            print('#', end='')
        print()


n = int(input('Masukkan n: '))

# tampilkan # sejumlah n secara vertikal
print('Pagar Vertikal')
pagar_vertikal(n)
print('Pagar Horizontal')
pagar_horizontal(n)
print('Persegi')
persegi(n)
print('Segitiga kiri')
segitiga_kiri(n)
print('Segitiga kanan')
segitiga_kanan(n)
print('Persegi bolong')
persegi_bolong(n)
print('Huruf X')
huruf_x(n)
print('Tanda plus')
tanda_plus(n)
print('Karpet')
karpet(n)
