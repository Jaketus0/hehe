bilangan = int(input('Masukkan sebuah bilangan: '))

# 10, 11, 12, 18, 19, 20, 21, 22,
satuan = bilangan % 10
# if satuan == 0 or satuan == 1 or satuan == 2 or satuan == 8 or satuan == 9:
if satuan in [0, 1, 2, 8, 9]:
    print(True)
else:
    print(False)
