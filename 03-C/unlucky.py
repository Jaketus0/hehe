# input
bilangan1 = int(input('Masukkan bilangan 1: '))
bilangan2 = int(input('Masukkan bilangan 2: '))
bilangan3 = int(input('Masukkan bilangan 3: '))

# proses dan output
if bilangan1 == 13:
    print('0')
elif bilangan2 == 13:
    print(bilangan1)
elif bilangan3 == 13:
    print(bilangan1 + bilangan2)
else:
    print(bilangan1 + bilangan2 + bilangan3)
