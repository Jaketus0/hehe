nama_file = 'data.py'
handle = open(nama_file, 'w') #read only

isi_file = input('masukan si file: ')
handle.write(isi_file) #overwrite
handle.close