import prima

# input user
batas = int(input('Masukkan batas: '))
for i in range(1, batas+1):
    hasil = prima.cek_prima(i)
    if hasil == True:
        print(i)
