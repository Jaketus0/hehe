print("1.Ascending(kecil ke besar)\n2.Descending(besar ke kecil)")
pilih = int(input("Pilih: "))
angkas = []

if pilih == 1:
    jlh = int(input("Jumlah angka: "))
    for i in range(jlh):
        angka = float(input("Masukkan angka: "))
        angkas.append(angka)
    sorted_list = sorted(angkas)
elif pilih == 2:
    jlh = int(input("Jumlah angka: "))
    for i in range(jlh):
        angka = float(input("Masukkan angka: "))
        angkas.append(angka)
    sorted_list = sorted(angkas, reverse=True)

print("Hasil pengurutan:", sorted_list)
