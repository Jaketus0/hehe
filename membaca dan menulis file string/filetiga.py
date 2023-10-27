keyword = input('masukan kata yang dicari =  ')

#case insensitive = tidak peduli huruf besar dan kecil
keyword = keyword.lower()

nama_file = 'data.txt'
handle = open(nama_file, 'r') #read only
jumlah = 0

#baca dengan for in
for baris in handle:
    baris = baris.lower()
    jumlah += baris.count(keyword)
print(f'ditemukan{jumlah} kata {keyword}')

handle.close()