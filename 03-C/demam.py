# input
suhu = float(input('Masukkan suhu: '))

# deman atau tidak? deman jika >= 38
if suhu < 34.0:
    print('Mati kedinginan')
elif 34.0 <= suhu <= 37.0:
    print('Suhu tubuh normal')
elif 37.1 <= suhu <= 40.0:
    print('Demam')
else:
    print('Mati kepanasan')


'''
coba untuk tambahkan kemungkinan:
<34 = mati kedinginan
34-37 = aman
37-40 = demam
>40 mati kepanasan
'''
