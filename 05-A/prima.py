def cek_prima(n):  # => True/False
    # prima => hanya habis dibagi 1 dan n => pembaginya cuma ada 2
    pembagi = 0
    for i in range(1, n+1):
        if n % i == 0:
            pembagi = pembagi + 1
    if pembagi == 2:
        return True
    else:
        return False


if __name__ == "__main__":
    # program utama
    # input user
    print("Program pengecekan bilangan prima")
    n = int(input('Masukkan bilangan: '))
    # proses
    hasil = cek_prima(n)  # true/false
    # output
    if hasil == True:  # hasilnya true/false
        print(f'{n} adalah bilangan Prima')
    else:
        print(f'{n} bukan bilangan Prima')
