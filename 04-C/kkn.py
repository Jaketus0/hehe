def seleksi_kkn(sks):
    # return True: jika bisa ambil kkn, sks >= 110
    # return False: jika sks < 110
    if sks >= 110:
        return True
    else:
        return False


# program utama
# input sks yang sudah diambil
sks = int(input('Masukkan jumlah sks yang sudah ditempuh: '))
# proses seleksi
hasil_seleksi = seleksi_kkn(sks)
# output
if hasil_seleksi == True:
    print('Boleh mengambil KKN')
else:
    print('Belum boleh mengambil KKN')
