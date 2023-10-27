import re 

#bac isi file txt dalam bentuk string
def baca_file(nama_file): 
    handle= open(nama_file)
    artikel= handle.read()
    return artikel


def proses_regex(artikel): 
    #pattern= "[A-Z][a-z]+"
    pattern= "Penyidik"
    #coba dengan fungsi search => yang pertama ketemu
    # hasil= re.findall(pattern,artikel)

    #pakai findall => ketemu semua, dalam bentuk list 
    hasil= re.findall(pattern,artikel)
    # print(f'Ditemukan {len(hasil)} kata Penyidik')
    return hasil

#program utama 
#minta input nama file 
nama_file= input('nama file: ')
#proses 
artikel= baca_file(nama_file)
print(artikel)
hasil= proses_regex(artikel)
#output
print(hasil)

