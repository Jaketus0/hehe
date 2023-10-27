# baca semua isi filenya dalam bentuk string
nama_file = 'data.txt'
handle = open(nama_file, 'r+')  # read sekaligus overwrite
isi_file = handle.read()
isi_file = isi_file.lower()
handle.close()

# input user
kata_asli = input('Masukkan kata yang akan diganti: ')
kata_asli = kata_asli.lower()

# cari apakah kata yang mau diganti ada?
if isi_file.count(kata_asli) == 0:
    # tidak ada.. batal
    print(f'Kata {kata_asli} tidak ada di dalam file!')
else:
    # kalau ada, lakukan penggantian dengan metode replace
    kata_ganti = input('Masukkan kata pengganti: ')
    kata_ganti = kata_ganti.lower()
    handle = open(nama_file, 'w')
    isi_file = isi_file.replace(kata_asli, kata_ganti)
    # tulis ke file
    handle.write(isi_file)
    handle.close()
