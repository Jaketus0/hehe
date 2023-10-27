# input
masukan = input('Masukkan angka positif (maks 9999):')

# proses mendapatkan ribuan, ratusan, puluhan, satuan
# ribuan = masukan // 1000
# ratusan = masukan // 100 - ribuan * 10
# puluhan = masukan // 10 - ratusan * 10 - ribuan * 100
# satuan = masukan % 10

# ribuan = masukan // 1000
# masukan = masukan % 1000
# ratusan = masukan // 100
# masukan = masukan % 100
# puluhan = masukan // 10
# masukan = masukan % 10
# satuan = masukan

total = 0
for number in masukan:
    total = total + int(number)

# output
print(f'Hasil penjumlahan semua digit adalah: {total}')
