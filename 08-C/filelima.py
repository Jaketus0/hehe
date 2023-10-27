# baca isi file dulu
nama_file = 'data.txt'
handle = open(nama_file, 'r')  # read only
isi_file = handle.read()

print('Isi file sekarang: ')
print(isi_file)
handle.close()

# setiap nambah baris, perlu enter apa nggak
perlu_enter = True
# ngecek apakah karakter terakhir adalah enter?
if isi_file[-1] == '\n':
    perlu_enter = False

# tambahkan satu baris di belakang
tambahan = input('Masukkan tambahan baris: ')
if perlu_enter:
    tambahan = '\n' + tambahan

# simpan
handle = open(nama_file, 'a')
handle.write(tambahan)
handle.close()
