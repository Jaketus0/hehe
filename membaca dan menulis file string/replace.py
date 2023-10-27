#baca isi file dulu
nama_file = 'text.txt'
handle = open(nama_file, 'r')
isi_file = handle.read()

#setiap nambah baris, perlu enter apa nggak
perlu_enter = True
#ngecek apakah karakter terakhir adalah enter?
if isi_file[-1] == '\n':
    perlu_enter = False

#tambahkan satu baris dibelakang
tambahan = input('Masukkan tambahan baris : ')
if perlu_enter:
    tambahan= '\n' + tambahan
#mode :
#1. mode a (appen) -> mau nambahin

handle = open(nama_file, 'a')
handle.write(tambahan)
handle.close()

#simpan
handle = open(nama_file, '')

#replace
kalimat = 'musik mudik kiwi'
kalimat.replace('musik','masak')

