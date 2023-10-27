nama_file = 'data.txt'
handle = open(nama_file, 'r')
isi_file = handle.read()

print('isi file sekarang: ')
print(isi_file)
handle.close

#setiap nambah baris
perlu_enter = True
if isi_file[-1] == '\n':
    perlu_enter = False

#tambahkan satu baris
tambahan = input('masukan tambahan baris: ')
if perlu_enter:
    tambahan = '\n' + tambahan

#simpan
handle = open(nama_file,'a')
handle.write(tambahan)
handle.close()

