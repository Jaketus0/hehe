# input
bilangan = int(input('Masukkan sebuah bilangan: '))

# jika positif
if bilangan > 0:
    print('Positif')
# negatif
elif bilangan < 0:
    print('Negatif')
else:  # bisa juga -> elif bilangan == 0:
    print('Nol')
