jumlah = int(input('Berapa biodata: '))
start = 1
namafile = 'biodata.txt'
handle = open(namafile, 'a')
nama=[]
umur=[]
alamat=[]
for i in range(jumlah):
    print(f'Biodata {start}: ')
    isinama = input('Nama: ')
    isiumur = int(input('Umur: '))
    isialamat = input('Alamat: ')
    nama.append(isinama)
    umur.append(isiumur)
    alamat.append(isialamat)
    handle.write(f'Nama: {isinama}\nUmur: {isiumur}\nAlamat: {isialamat}\n\n')
    start += 1
handle.close()
