# input
suhu = float(input('Masukkan suhu badan: '))

# kriteria demam: >= 38
if suhu < 32:
    print('Meninggal')
elif 32 <= suhu < 36:
    print('Bahaya Hipotermia')
elif 36 <= suhu < 38:
    print('Suhu tubuh normal')
elif 38 <= suhu <= 41:
    print('Demam')
else:
    print('Meninggal')  # False
