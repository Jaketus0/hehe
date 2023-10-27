# input
angka = input('Masukkan angka (0-9999): ')

# proses
# ribuan = angka // 1000
# angka = angka % 1000
# ratusan = angka // 100
# angka = angka % 100
# puluhan = angka // 10
# satuan = angka % 10
# total = ribuan + ratusan + puluhan + satuan

total = 0
for digit in angka:
    total = total + int(digit)

# output
print('Total semua digit: ', total)
