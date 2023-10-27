nama_file = 'data.txt'
handle = open(nama_file, 'w')  # write

isi_file = input('Masukkan isi file: ')
handle.write(isi_file)  # overwrite
handle.close()
