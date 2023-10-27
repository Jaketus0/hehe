nota = {
    "nama_toko": "maju jaya",
    "alamat": "jl kuburan 34",
    "pembeli": "bambang",
    "tanggal": "9 Mei 2023",
    "belanja": [
        {
            "no": 1,
            "kode": "P001",
            "harga_satuan": 1500,
            "jumlah_beli": 2,
            "subtotal": 3000,
            "nama": "Pensil Biasa",
        },
        {
            "no": 2,
            "kode": "PH001",
            "harga_satuan": 5500,
            "jumlah_beli": 2,
            "subtotal": 11000,
            "nama": "Pensil 2B",
        },
    ],
}

print(nota["nama_toko"])
print(nota["pembeli"])
total_jumlah_beli = 0
for barang in nota["belanja"]:
    total_jumlah_beli = total_jumlah_beli + barang["jumlah_beli"]
print(total_jumlah_beli)
total_beli = 0
for barang in nota["belanja"]:
    total_beli = total_beli + barang["subtotal"]
print(f"Jumlah pembelian: {total_beli}")
total_bayar = total_beli * 0.8
print(f"Harus membayar: {total_bayar}")
