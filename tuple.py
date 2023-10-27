data = {
    'nama' : 'Maju Jaya',
    'no_nota' : 1, 
    'kepada' : 'Bambang',
    'barang' : [
        (1, 'Penghapus', 1000, 3, 3000),
        (2, 'Penggaris', 2000, 10, 2000),
        # ('no' : 3, 'nama_barang' : 'rautan', 'harga_satuan' : 4500, 'jumlah_beli' : 3, 'subtotal' : 13500)
    ],
}
for key, value in data.items(): 
    print(f'{key}: {value}')
