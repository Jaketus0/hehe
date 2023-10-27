class Mobil: 
    def __init__(self, merek, tipe):
        self.merek_mobil = merek
        self.tipe_mobil = tipe
        self.kapasitas_bbm = int()
        self.jenis_bahanbakar = str()
    def set_kapasitasbbm(self, kapasitas_bbm): 
        if kapasitas_bbm > 0:
            self.kapasitas_bbm = kapasitas_bbm
            return True
        else: 
            return False
    def set_jenis(self, jenis):
        self.jenis = jenis
        return True
    def get_jenisbahanbakar(self, jenis_bahanbakar):
        self.jenis_bahanbakar = jenis_bahanbakar
        return True
    def get_merek(self):
        return self.merek_mobil
    def get_tipe(self): 
        return self.tipe_mobil
    def get_kapasitas(self): 
        return self.kapasitas_bbm
    def get_jenis(self): 
        return self.jenis_bahanbakar
    def printinfo(self): 
        print('==========ingpo========')
        print(f'merek:{self.merek_mobil}')
        print(f'tipe:{self.tipe_mobil}')
        print(f'bahan bakar:{self.jenis_bahanbakar}')
        print(f'kapasitas:{self.kapasitas_bbm}')
    def isi_bbm(self,harga):
        if self.kapasitas_bbm == 0:
            print("ERROR kapasitas BBM atau jenis bahan bakar belum diinputkan")
            return False
        elif harga > 0:
            total = harga * self.kapasitas_bbm
            print("total harga: ", total) 
        else:
            return False 
if __name__ == "__main__":
    m1 = Mobil("tayo","via")
    m1.printinfo()
    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.set_jenis("Bensin")
    mobil2.set_kapasitasbbm(20)
    mobil2.printinfo()
    m1.isi_bbm(14500)
    mobil2.isi_bbm(14500)