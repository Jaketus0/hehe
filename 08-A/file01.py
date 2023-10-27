nama_file = 'data.txt'
handle = open(nama_file, 'r')  # membuka dalam mode read-only
isi_file = handle.read()  # membaca isi keseluruhan
print(isi_file)
handle.close()  # harus ditutup supaya file bebas dari pegangan program ini
