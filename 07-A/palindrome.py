def cek_palindrome(kalimat):
    # ubah semua ke huruf kecil
    kalimat = kalimat.lower()

    # hapus yang bukan alfabet (bukan a-z)
    kalimat_bersih = ''
    for karakter in kalimat:
        if karakter.isalpha():
            kalimat_bersih = kalimat_bersih + karakter

    # buat kebalikannya
    kalimat_bersih_balik = kalimat_bersih[::-1]

    # cek sama atau tidak
    if kalimat_bersih == kalimat_bersih_balik:
        return True
    else:
        return False


# program utama
kalimat = input('Masukkan kalimat: ')
hasil = cek_palindrome(kalimat)
if hasil == True:
    print('Palindrome!')
else:
    print('Bukan Palindrome!')
