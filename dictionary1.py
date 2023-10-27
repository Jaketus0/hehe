khs={
    '71220871' : ['Tekkom','Jarkom','Logmat'],
    '71210872' : ['Mattek','Alpro','IMK'],
}
# print(khs['71220871'])#semua dafftar kuliahnya 
# print(khs['71220871'][0]) #1 saja 
for key in khs.keys():
    print(f'NIM: {key}, Matkul: {khs[key]}') #untuk nampilin semua (NIM dan Matkulnya)
print()
khs['71210872'].append('Statistik') #untuk nambah khs
print(khs)
print()
del khs['71210872'][0] #untuk hapus index 0
print(khs)


daftargame= { 
    "jumlah_game": 0,
    "daftar_game": []
}

daftargame["jumlah_game"]= 3

daftargame["daftar_game"].append({
    "nama_game": "Valorant",
    "tipe_game": "First Person",
    "pc_hp": "Game PC",
    "jumlah_pemain_dalam_1_team": "5 orang",
    "jumlah_hero": "22 Agents",
    "role": ["Sentinels", "Controller", "Initiators", "Duelist"]
})
daftargame["daftar_game"].append({
    "nama_game": "Identity V",
    "tipe_game": "Third Person",
    "pc_hp": ["Game PC", "Game hp"],
    "jumlah_pemain_dalam_1_team": "4 orang",
    "jumlah_hero": "64 Character",
    "role": ["survivor", "hunter"]
})
daftargame["daftar_game"].append({
    "nama_game": "Mobile Legend",
    "tipe_game": "Third Person",
    "pc_hp": "Game hp",
    "jumlah_pemain_dalam_1_team": "5 orang",
    "jumlah_hero": "120 Hero",
    "role": ["Marksman", "Assassin", "Mage", "Tank", "Fighter", "Support"]
})

print("Jumlah game: ", daftargame["jumlah_game"])
print("Game First Person: ")
for i in daftargame ["daftar_game"]: 
    if i ["tipe_game"] == "First Person":
        print(i["nama_game"])
print("Game dengan 5 pemain: ")
for i in daftargame["daftar_game"]: 
    if i ["jumlah_pemain_dalam_1_team"] == "5 orang": 
        print(i["nama_game"])
print("Game pc: ")
for i in daftargame["daftar_game"]: 
    if i ["pc_hp"] == "Game PC": 
        print(i["nama_game"])
print("Game dengan role terbanyak: ")
max_role_game = max(daftargame["daftar_game"], key=lambda game: len(game["role"]))
print(max_role_game["nama_game"])
print("Role yang ada di game Valorant: ")
for i in daftargame["daftar_game"]:
    if i["nama_game"] == "Valorant":
        roles_str = ", ".join(i["role"])
        print(roles_str)