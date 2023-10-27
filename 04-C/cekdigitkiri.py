'''
Triple pythagoras (memenuhi salah satu ini)
a**2 + b**2 = c**2
b**2 + c**2 = a**2
c**2 + a**2 = b**2
'''


def cek(a, b, c):  # return True/False
    if a**2 + b**2 == c**2:
        print(f'{a}**2 + {b}**2 = {c}**2')
        return True
    elif b**2 + c**2 == a**2:
        print(f'{b}**2 + {c}**2 = {a}**2')
        return True
    elif c**2 + a**2 == b**2:
        print(f'{c}**2 + {a}**2 = {b}**2')
        return True
    else:
        return False


# program utama
# input
a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
c = int(input('Masukkan c: '))

hasil = cek(a, b, c)
if hasil == True:
    print('Merupakan triple pythagoras')
else:
    print('Bukan triple pythagoras')
