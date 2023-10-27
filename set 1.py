data= [1,3,4,5,2,3,2,4,5,5,4,1,3,7]
data_unik= set()
#{library} [list] (tuple)
#MASALAH: masukkan dalam data unik dalam posisi tidak ada yang sama 
#masukkan dalam data unik dalam posisi tidak ada yang sama 
#cara 1: perulangan biasa 
hasil= []
for nilai in data: 
    if nilai not in hasil: 
        hasil.append(nilai)
print(hasil)

#cara 2: pakai set 
hasil= set()
for nilai in data: 
    hasil.add(nilai)
# print(hasil) #print bentuk dict 
print(list(hasil)) #print bentuk list   