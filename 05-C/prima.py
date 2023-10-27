import math


def is_prime(number):
    pembagi = 0
    for i in range(1, number+1):  # pencarian hanya sampai akar n
        if number % i == 0:
            pembagi += 1  # pembagi = pembagi + 1
    if pembagi == 2:
        return True
    else:
        return False


# program utama
bawah = int(input('Masukkan batas bawah: '))
atas = int(input('Masukkan batas atas: '))

for i in range(bawah, atas+1):
    hasil = is_prime(i)
    if hasil:
        print(i)
