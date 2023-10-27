# tabel pangkat


def tabel_pangkat(n, pangkat):
    # buat dictionary
    hasil = dict()

    # insert key 1...n dan value-nya
    for i in range(1, n + 1):
        hasil[i] = i**pangkat
    # return
    return hasil


# program utama
# input n
n = int(input("Masukkan n: "))
pangkat = int(input("Masukkan pangkat: "))
hasil = tabel_pangkat(n, pangkat)
print(hasil)
