import random


def generate_angka(bawah, atas):
    angka_komputer = random.randrange(bawah, atas)
    return angka_komputer


# program utama
# input level
langkah = 6
angka_komputer = 0
level = int(input('Masukkan level 1/2/3: '))
if level == 1:  # easy
    print('Level Easy [0..100]')
    angka_komputer = generate_angka(0, 100)
    langkah = 6
elif level == 2:  # intermediate
    print('Level Intermediate [0..1000]')
    angka_komputer = generate_angka(0, 1000)
    langkah = 10
else:  # hard
    print('Level Hard [0..1000000]')
    angka_komputer = generate_angka(0, 1_000_000)
    langkah = 12

tebakan = False

hasil = False  # kalah

while tebakan == False:  # selama tebakan masih False, ulangi terus
    if langkah == 0:
        break
    tebakan_user = int(input('Masukkan tebakan anda: '))
    langkah = langkah - 1
    if tebakan_user == angka_komputer:
        tebakan = True
        hasil = True
        break
    else:
        if tebakan_user > angka_komputer:
            print('Tebakan anda terlalu besar')
        else:
            print('Tebakan anda terlalu kecil')
        print('Tebakan anda masih salah!  Silahkan coba lagi....')
if hasil == True:
    print(f'Selamat, anda menang. Tebakan anda benar. Sisa: {langkah}')
else:
    print("Anda kalah, sudah kehabisan langkah")
