def tukar(a=10, b=15):
    temp = a # temp = 10
    a = b # a = 15
    b = temp # b = 10
    return a, b

a = 10
b = 15
print('sebelum ditukar')
print('a: ', a)
print('b: ', b)

a, b = tukar(a, b) # tukar(10, 15)

print('setelah ditukar')
print('a: ', a)
print('b: ', b)
