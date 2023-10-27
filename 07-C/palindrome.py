def cek_palindrome(kalimat):
    # palindrome hanya mengecek alfabet (A-Z dan a-z)
    # konversi semuanya ke huruf kecil
    kalimat = kalimat.lower()
    # buang semua yang bukan alfabet
    hasil = ''
    for karakter in kalimat:
        if karakter.isalpha():
            hasil = hasil + karakter

    balik = hasil[::-1]
    if hasil == balik:
        print('Palindrome!')
    else:
        print('Bukan palindrome!')


kalimat = input('Masukkan sebuah kalimat: ')
cek_palindrome(kalimat)
