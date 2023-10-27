a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
c = int(input('Masukkan c: '))

total = 0

# jika beda semua = total semua
if a != b and a != c and b != c:
    total = a + b + c
# jika semua sama
elif a == b and a == c and b == c:
    total = 0
elif a == b:
    total = c
elif a == c:
    total = b
else:
    total = a

print(total)
