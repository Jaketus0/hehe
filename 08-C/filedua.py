nama_file = 'data.txt'
# windows
# nama_file = 'D:\\Android\\data.txt'

# linux
# nama_file = '/var/www/data.txt'

handle = open(nama_file, 'r')  # read only mode teks
# mode = r, w, a, b->binary
# baca semua
# 1. handle.readlines() => list berisi semua baris
# 2. handle.read() => string
# 3. handle.readline() => string, 1 baris di posisi sekarang
hasil = handle.readlines()
print(hasil)
print(f'Ada {len(hasil)} baris')
