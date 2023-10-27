namafile= input('Masukkan nama file: ')
handle= open(namafile, 'a')
n=int(input('Tambah berapa data: '))
for i in range(1,n+1): 
    data= input('Masukkan data: ')
    handle.write(data + '\n')
handle.close()