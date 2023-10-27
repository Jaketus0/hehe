from "05T" import Rekening

r1 = Rekening(1234,"agus",10000)
r1.simpan_uang(75000)
r1.ambil_uang(50000)
print(r1.saldo_awal)

r2 = Rekening(5678,"tuti", 500000)
r2.simpan_uang(150000)
print(r2.saldo_awal)