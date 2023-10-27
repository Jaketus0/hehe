nama_file = 'data.txt'
# windows
#nama_file = 'D:\\android\\data.txt'

#linux
##nama_file = '/var/www/data.txt'

handle = open(nama_file, 'r') #read only
# mode = r, w, a, b = binary

# 1. handle.readlines() = list berisi semua baris
# 2. handle.read() = ambil semua baris / string
# 3. handle. readline() = ambil baris 1 / list
hasil = handle.readlines()
print(hasil)
print(f'Ada {len(hasil)} baris')