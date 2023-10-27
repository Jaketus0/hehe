# input
masukan = int(input('Masukkan angka positif (1000 - 9999):'))
# proses

depan = masukan // 1000
belakang = masukan % 10
total = depan + belakang

# output
print(f'Total: {total}')
