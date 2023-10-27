khs = {
    "71200183": ["Tekkom", "Jarkom", "Logmat"],
    "71193450": ["PAK", "Tekkom", "Logmat"],
}

for key in khs.keys():
    print(f"NIM: {key}, Matkul: {khs[key]}")

print()

khs["71193450"].append("IMK")
print(khs)

print()

del khs["71200183"][0]

print(khs)
