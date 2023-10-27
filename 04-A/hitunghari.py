# tidak perlu return, lakukan print di dalam fungsi sebagai output
def hitung_hari(sekarang, n):
    n = n % 7
    hari = 0
    if sekarang == 'senin':
        hari = 0
    elif sekarang == 'selasa':
        hari = 1
    elif sekarang == 'rabu':
        hari = 2
    elif sekarang == 'kamis':
        hari = 3
    elif sekarang == 'jumat':
        hari = 4
    elif sekarang == 'sabtu':
        hari = 5
    else:
        hari = 6

    hari = (hari + n) % 7

    if hari == 0:
        print('senin')
    elif hari == 1:
        print('selasa')
    elif hari == 2:
        print('rabu')
    elif hari == 3:
        print('kamis')
    elif hari == 4:
        print('jumat')
    elif hari == 5:
        print('sabtu')
    elif hari == 6:
        print('minggu')


# input hari sekarang
# senin, selasa, rabu, kamis, jumat, sabtu, minggu
sekarang = input('Masukkan nama hari sekarang: ')
n = int(input('Mau berapa hari kedepan?: '))
hitung_hari(sekarang, n)
'''
selasa, 100 => kamis   rabu, 49 ==> rabu
jumat, 8 => sabtu
kamis, 55 => rabu
minggu, 8 => senin
rabu, 1000 => selasa
'''
