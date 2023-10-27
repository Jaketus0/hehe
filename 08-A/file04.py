nama_file = 'buah.txt'
handle = open(nama_file, 'a')  # mode append (sambung di belakang)

nama_buah = input('Masukkan nama buah: ')
handle.write('\n' + nama_buah)

handle.close()
