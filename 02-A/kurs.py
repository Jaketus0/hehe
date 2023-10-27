# input
rupiah = int(input('Masukkan Rp: '))

# proses
usd = rupiah / 14900
yen = rupiah / 130
eur = rupiah / 16700
aud = rupiah / 11500

# output
print('Rupiah\t\tUSD\t\tYen\t\tEur\t\tAUD')
print('%d\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f' % (rupiah, usd, yen, eur, aud))
