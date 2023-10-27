def n_hari_berikutnya(nama, n):  # nama => 'senin', 'selasa' dst...
    n = n % 7
    '''
    senin = 0  
    selasa = 1
    rabu = 2
    kamis = 3
    jumat = 4
    sabtu = 5
    minggu = 6
    '''
    bobot = 0
    if nama == 'selasa':
        bobot = 1
    elif nama == 'rabu':
        bobot = 2
    elif nama == 'kamis':
        bobot = 3
    elif nama == 'jumat':
        bobot = 4
    elif nama == 'sabtu':
        bobot = 5
    elif nama == 'minggu':
        bobot = 6

    total = (bobot + n) % 7
    if total == 0:
        print('senin')
    elif total == 1:
        print('selasa')
    elif total == 2:
        print('rabu')
    elif total == 3:
        print('kamis')
    elif total == 4:
        print('jumat')
    elif total == 5:
        print('sabtu')
    elif total == 6:
        print('minggu')


nama = input('Masukkan nama: ')
n = int(input('Berapa hari kemudian?: '))
n_hari_berikutnya(nama, n)
