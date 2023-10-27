import os #untuk mengakses file dan direktori dalam python 
path = 'D:\\Python\\'
exist = os.path.exists(path)
folder_path = "."  # Ganti dengan path folder yang ingin Anda periksa
txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]
print("File TXT yang ada di dalam folder:")
for file in txt_files:
    print(file)
#folder_path dengan path folder yang ingin Anda periksa. Misalnya, jika folder yang ingin Anda periksa berada di direktori yang sama dengan program ini, maka bisa menggunakan "." untuk merepresentasikan folder saat ini.
#Program ini menggunakan os.listdir(folder_path) untuk mendapatkan daftar semua file dan folder di dalam folder_path. Kemudian, menggunakan list comprehension dan metode str.endswith() untuk memfilter hanya file dengan ekstensi .txt.
print('Program menambah dan menghapus file')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('1. Menambah file\n2. Menghapus file')
pil = int(input('Masukkan pilihan : '))
if pil == 1: 
    namafile = input('Nama file : ')
    inputan = int(input('Berapa item : '))
    if namafile is exist: 
        handle = open(namafile, 'a')
    else: 
        handle = open(namafile, 'w')
    start = 1
    for i in range(1,inputan+1): 
        isi = input(f'Masukkan daftar {start}: ')
        handle.write(f'{start}. {isi}\n')
        start +=1 
        
    handle.close()
    print('Daftar sudah berhasil ditambahkan')
        
elif pil == 2: 
    namafile = input('Nama file yang mau dihapus: ')
    if os.path.exists(namafile):
        os.remove(namafile)
        print(f'File {namafile} sudah dihapus')
    else: 
        print(f'File tidak ditemukan') 