"""
kk = {
    "nomor":73081.....,
    "kepala_keluarga" : "Andi Tantu",
    ....

}
"""

koleksi_buku = {
    "pemilik": "yuan lukito",
    "daftarbuku": [
        {
            "judul": "detective conan",
            "penerbit": "elex media",
            "penjual": ["gramedia", "togamas"],
        },
        {
            "judul": "pemrograman python",
            "penerbit": 'O"Reilly',
            "penjual": ["gramedia"],
        },
    ],
}

pemilik = koleksi_buku["pemilik"]  # siapa pemiliknya?
print(f"Pemiliknya adalah: {pemilik}")
jumlah_buku = len(koleksi_buku["daftarbuku"])  # ada berapa bukunya?
print(f"Jumlah buku: {jumlah_buku}")
for buku in koleksi_buku["daftarbuku"]:  # apa saja judulnya?
    print(f'{buku["judul"]} dijual di {buku["penjual"]}')

"""
1. siapa kepala keluarganya?
2. ada berapa orang dalam kk?
3. tampilkan nama dan agamanya masing-masing
4. tampilkan siapa saja yang sudah nikah
5. tampilkan siapa saja nama anak-anaknya
6. apakah ada yang WNA?
7. siapa saja yang tahun lahirnya > 2000?
"""
