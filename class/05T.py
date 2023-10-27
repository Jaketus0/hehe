class Rekening:
    def __init__ (self, no_rekening,nama,saldo_awal):
        self.no_rekening = no_rekening #variabel global
        self.nama = nama
        self.saldo_awal = saldo_awal
        self.daftar_transaksi = []

    def simpan_uang (self, setoran):
        if setoran > 0:
            self.saldo_awal = self.saldo_awal + setoran
            return True
        else: 
            return False
        
    def ambil_uang (self, penarikan ):
        if penarikan > 0 and self.saldo_awal > penarikan:
            self.saldo_awal = self.saldo_awal - penarikan 
            return True
        else: 
            return False
        
r1 = Rekening(1234,"agus",10000)
r1.simpan_uang(75000)
r1.ambil_uang(50000)
print(r1.saldo_awal)
