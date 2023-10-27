nama_file = 'transkrip.txt'
handle = open(nama_file, 'r')
no_baris = 1
print('Daftar Matakuliah yang diambil: ')
totalsks = 0
totalbobot = 0
sks = 0
matakuliah = ''
harus_diulang = ''
for baris in handle:
    if no_baris % 3 == 1:
        print(baris, end='')
        matakuliah = baris.strip()
    if no_baris % 3 == 2:  # untuk baca sks
        totalsks = totalsks + int(baris)
        sks = int(baris)
    if no_baris % 3 == 0:  # untuk baca nilai A/B/C/D/E
        if baris.strip() == 'A':
            totalbobot = totalbobot + sks * 4
        elif baris.strip() == 'B':
            totalbobot = totalbobot + sks * 3
        elif baris.strip() == 'C':
            totalbobot = totalbobot + sks * 2
        elif baris.strip() == 'D':
            totalbobot = totalbobot + sks * 1
        elif baris.strip() == 'E':
            harus_diulang = harus_diulang + matakuliah + '\n'

    no_baris = no_baris + 1
print(f'Total SKS: {totalsks} sks')
print(f'IP Semester : {totalbobot/totalsks:.2f}')
print('Matakuliah ini harus diulang: ')
print(harus_diulang)
handle.close()
