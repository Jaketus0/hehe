nama_file = 'data.txt'
handle = open(nama_file, 'r')  # membuka dalam mode read-only

for baris in handle:
    if baris[0] == 'S':
        print(baris, end='')
handle.close()
