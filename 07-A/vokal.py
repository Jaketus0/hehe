def hitung_vokal(kalimat):
    vokal = 'aiueoAIUEO'  # siapkan daftar huruf vokal
    jumlah = 0
    for karakter in kalimat:  # cek satu-persatu karakter mulai dari depan
        if karakter in vokal:  # jika ada yang termasuk vokal, masuk dalam hitungan
            jumlah = jumlah + 1
    return jumlah


def hitung_whitespace(kalimat):
    jumlah = 0
    for karakter in kalimat:
        if karakter.isspace() == True:  # mengecek apakah karakter termasuk whitespace?
            jumlah = jumlah + 1
    return jumlah


def hitung_konsonan(kalimat):
    # konsonan = alfabet (a-z, A-Z) - vokal (aiueo AIUEO)
    vokal = 'aiueoAIUEO'
    jumlah = 0
    for karakter in kalimat:
        if karakter not in vokal and karakter.isalpha():
            jumlah = jumlah + 1
    return jumlah


# program utama
# input
kalimat = input('Masukkan sebuah kalimat: ')

# proses
jumlah_vokal = hitung_vokal(kalimat)
jumlah_whitespace = hitung_whitespace(kalimat)
jumlah_konsonan = hitung_konsonan(kalimat)
# output
print(f'Jumlah huruf vokal: {jumlah_vokal}')
print(f'Jumlah huruf whitespace: {jumlah_whitespace}')
print(f'Jumlah huruf konsonan: {jumlah_konsonan}')
