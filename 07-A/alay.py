'''
a A = 4
i I = 1
e E = 3
o O = 0
j J = 7
g G = 9
b = 6
r R = 2
s S = 5
B = 8
'''


def translate_to_alay(kalimat):
    huruf_alay = 'aAiIeEoOjJgGbrRsSB'
    hasil_alay = '441133007799622558'
    hasil = ''
    for karakter in kalimat:
        if karakter in huruf_alay:  # harus diubah
            posisi = huruf_alay.index(karakter)
            hasil = hasil + hasil_alay[posisi]
        else:
            hasil = hasil + karakter  # tidak perlu diubah
    return hasil


# program
kalimat = input('Masukkan kalimat: ')
hasil = translate_to_alay(kalimat)
print(hasil)
