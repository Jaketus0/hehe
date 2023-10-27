# Membuat dictionary untuk informasi kartu keluarga
kk = {
    "kepala_keluarga": "Bagus",
    "jumlah_anggota": 0,
    "anggota_keluarga": []
}

# Menambahkan informasi kepala keluarga dan jumlah anggota
kk["kepala_keluarga"] = "Bagus"
kk["jumlah_anggota"] = 4

# Menambahkan informasi anggota keluarga ke dalam list dict
kk["anggota_keluarga"].append({
    "nama": "Bagus",
    "agama": "Islam",
    "status_nikah": "Menikah",
    "pasangan": "Mawar",
    "anak": ["Suri", "Suram"],
    "wna": "Zimbabwe",
    "tahun_lahir": 1945
})
kk["anggota_keluarga"].append({
    "nama": "Mawar",
    "agama": "Katolik",
    "status_nikah": "Menikah",
    "pasangan": "Bagus",
    "anak": None,
    "wna": "Thailand",
    "tahun_lahir": 1940
})
kk["anggota_keluarga"].append({
    "nama": "Suri",
    "agama": "Buddha",
    "status_nikah": "Belum Menikah",
    "pasangan": None,
    "anak": None,
    "wna": "Dubai",
    "tahun_lahir": 1970
})
kk["anggota_keluarga"].append({
    "nama": "Suram",
    "agama": "Hindu",
    "status_nikah": "belum Menikah",
    "pasangan": None,
    "anak": None,
    "wna": "China",
    "tahun_lahir": 2001
})

print(kk) 
# Menampilkan informasi yang diminta
print("Kepala keluarga:", kk["kepala_keluarga"])
print("Jumlah anggota keluarga:", kk["jumlah_anggota"])
print("Nama dan agama masing-masing anggota:")
for anggota in kk["anggota_keluarga"]:
    print(anggota["nama"], "-", anggota["agama"])
print("Anggota keluarga yang sudah menikah:")
for anggota in kk["anggota_keluarga"]:
    if anggota["status_nikah"] == "Menikah":
        print(anggota["nama"])
print("Nama anak-anak dalam keluarga:")
for anggota in kk["anggota_keluarga"]:
    if anggota["anak"] is not None:
        for anak in anggota["anak"]:
            print(anak)
print("Ada yang WNA?")
for anggota in kk["anggota_keluarga"]:
    print(anggota["nama"], "-", anggota["wna"])
# for anggota in kk["anggota_keluarga"]:
#     if anggota["wna"] == "y":
#         print(anggota["nama"])
print("Nama anggota keluarga yang tahun lahirnya > 2000:")
for anggota in kk["anggota_keluarga"]:
    if anggota["tahun_lahir"] > 2000:
        print(anggota["nama"])

