cigars = int(input('Masukkan jumlah rokok: '))
weekend = input('Apakah weekend? (Y/N): ')
is_weekend = False

if weekend == 'Y' or weekend == 'y':
    is_weekend = True

if (is_weekend == True and cigars >= 40) or (is_weekend == False and 40 <= cigars <= 60):
    print('Sukses')
else:
    print('Gagal')
