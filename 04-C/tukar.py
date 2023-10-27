def tukar(a, b):
    temp = b
    b = a
    a = temp
    return a, b # tuple


a = int(input('Masukkan nilai a: '))
b = int(input('Masukkan nilai b: '))
print(f'Sebelum ditukar, a: {a}, b: {b}')
a, b = tukar(a, b)  # tukar(10, 15)
print(f'Setelah ditukar, a: {a}, b: {b}')
