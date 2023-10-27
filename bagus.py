# a,A = 4
# b = 6
# B = 8 
# s,S = 5
# e,E = 3 
# i,I = 1 
# o,O = 0
# g,G = 9

def translate(kalimat): 
    #daftar huruf asli dan nomor 
    asli= 'aAbBsSeEiIoOgG'
    nomor= '44685533110099'
    #cek satu persatu karakternya
    #for i in range(len(kalimat)): => menggunakan index 
    hasil= ''
    for karakter in kalimat:
        if karakter in asli:
            #harus direplace 
            idx= asli.index(karakter)
            hasil= hasil + nomor [idx]
        else:
            #tidak perlu direplace 
            hasil= hasil + karakter
    return hasil 
kalimat= input('Masukkan kalimat :  ')
hasil= translate(kalimat)
print(hasil)
