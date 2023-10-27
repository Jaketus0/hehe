#inisialisasi dictionary nota
nota = {
    'nama_toko': 'Gelora Aido Motor',
    'alamat': 'Jl. Raya Parakan No. 61A Pondok Benda, Pamulang',
    'no_telp': ['62255784252', '6225565741'],
    'tanggal': '14-09-2022',
    'nama_pembeli': '',
    'no_nota': 14,
    'total': 0,
    'pembelian': []
}

#input data pembeli
nama = input('Masukkan nama pembeli: ')
nota['nama_pembeli'] = nama

#input user barang yang dibeli
jumlah_barang = int(input('Jumlah barang yang dibeli: '))
total = 0 #inisialisasi variabel total sebelum digunakan
for i in range(jumlah_barang):
    nama_barang = input('Nama barang yang dibeli: ')
    banyaknya = int(input('Banyaknya: ')) #ubah input banyaknya menjadi integer
    harga_satuan = int(input('Harga Satuan Rp: '))
    subtotal = banyaknya * harga_satuan
    total = total + subtotal

    #buat dictionary untuk barang ini
    item_barang = {
        'banyaknya': banyaknya,
        'nama_barang': nama_barang,
        'harga_satuan': harga_satuan,
        'subtotal': subtotal
    }

    #masukkan ke dalam nota
    nota['pembelian'].append(item_barang)

#update total pembelian 
nota['total'] = total

#menampilkan hasil
print(nota)