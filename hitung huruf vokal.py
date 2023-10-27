def hitung_vokal(kalimat): 
    vokal = 'aAiIuUeEoO'
    jumlah = 0
    #cek satu persatu karakternya 
    for karakter in kalimat: 
        #jika karakter ada di dalam daftar huruf vokal maka akan bertambah 1 
        if karakter in vokal:
            jumlah+=1
    return jumlah 

def hitung_konsonan(kalimat): 
    vokal= 'aAiIuUeEoO'
    jumlah= 0 
    for karakter in kalimat:
        #konsonan adalah yang karakter yang tidak termasuk vokal, tapi masuk dalam alfabet  
        if karakter not in vokal and karakter.isalpha(): 
            jumlah+=1 
    return jumlah

def hitung_digit(kalimat): 
    digit= '0123456789'
    jumlah= 0 
    for karakter in digit:
        if karakter in digit: 
            jumlah+=1 
    return jumlah

def hitung_whitespace(kalimat): 
    jumlah= 0
    for karakter in kalimat: 
        if karakter.isspace(): 
            jumlah = jumlah + 1
    return jumlah
#program utama 
#input 
kalimat= input('Masukkan kalimat :')
#proses 
hasil= hitung_vokal(kalimat)
hasil2= hitung_konsonan(kalimat)
hasil3= hitung_digit(kalimat)
hasil4= hitung_whitespace(kalimat)
#output
print(f'Jumlah huruf vokal : {hasil}')
print(f'Jumlah huruf konsonan : {hasil2}')
print(f'Jumlah huruf digit : {hasil3}')
print(f'Jumlah huruf space : {hasil4}')