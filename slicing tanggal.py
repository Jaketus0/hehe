def parse_tanggal(tgl):
    return tgl[-2:] + '-' + tgl[5:7] + '-' + tgl[:4]

#program utama
tgl = '2021-11-31'
hasil = parse_tanggal(tgl)
print(f'konversi DD-MM-YYYY:{hasil}')