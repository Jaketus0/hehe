nama_file = 'data.txt'
# windows
#nama_file = 'D:\\android\\data.txt'

#linux
##nama_file = '/var/www/data.txt'

handle = open(nama_file, 'r') #read only
# mode = r, w, a, b = binary

n = 3
no_baris = 1

for baris in handle:
    if no_baris == n:
        print(baris) # jika tidak ingin ada enter maka print(baris, end=' ')
    no_baris += 1
# harus selal dilakukan
handle.close()