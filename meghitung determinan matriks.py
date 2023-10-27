# Input ukuran matriks
m = int(input("Masukkan jumlah baris matriks: "))
n = int(input("Masukkan jumlah kolom matriks: "))

# Inisialisasi matriks dengan nilai 0
mat = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)

# Input elemen-elemen matriks
print("Masukkan elemen-elemen matriks:")
for i in range(m):
    for j in range(n):
        mat[i][j] = float(input("Elemen matriks [{},{}]: ".format(i+1, j+1)))

# Mencetak matriks
print("\nMatriks yang dimasukkan:")
for i in range(m):
    for j in range(n):
        print(mat[i][j], end="\t")
    print()

# Menghitung determinan matriks
if m == n:
    det = 1
    for i in range(n):
        for j in range(i+1, n):
            factor = mat[j][i] / mat[i][i]
            for k in range(n):
                mat[j][k] -= factor * mat[i][k]
        det *= mat[i][i]
    print("\nDeterminan matriks =", det)
else:
    print("\nMatriks bukan matriks persegi, tidak dapat menghitung determinan.")
