nama_file = 'data.txt'
# windows
# nama_file = 'D:\\Android\\data.txt'

# linux
# nama_file = '/var/www/data.txt'

handle = open(nama_file, 'r')  # read only mode teks
# mode = r, w, a, b->binary

n = 3
no_baris = 1
for baris in handle:
    if no_baris == n:
        # hanya menampilkan baris ke-n saja
        print(baris, end='')
    no_baris = no_baris + 1

# harus selalu dilakukan
handle.close()
