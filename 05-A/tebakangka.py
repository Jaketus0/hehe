import random

'''
level 1 => 0-100,           5
      2 => 0-1000,          7
      3 => 0-1_000_000      10
'''


def generate_angka_komputer(batas):
    hasil = random.randrange(0, batas+1)
    return hasil


def game(angka_komputer, langkah):
    print("=== Program Tebak ===")
    menang = False
    while menang == False:
        tebakan = int(input("Masukkan tebakan anda: "))
        langkah = langkah - 1
        if tebakan == angka_komputer:
            menang = True
        else:
            print(
                f"Tebakan anda salah! Silahkan coba lagi. Sisa langkah: {langkah}")
            if tebakan > angka_komputer:
                print("Tebakan anda terlalu besar")
            else:
                print("Tebakan anda terlalu kecil")
            if langkah == 0:
                break
    
    print("Angka komputer: ", angka_komputer)
    if menang == True:
        print(f"Tebakan anda benar. Anda menang! Sisa langkah: {langkah}")
    else:
        
        print("Anda kalah. Langkah anda habis!")

    # program utama
    # 1. generate angka random
level = int(input("Masukkan level: 1/2/3: "))
if level == 1:
    batas = 100
    langkah = 5
elif level == 2:
    batas = 1000
    langkah = 7
else:
    batas = 1_000_000
    langkah = 10

angka_komputer = generate_angka_komputer(batas)
game(angka_komputer, langkah)
