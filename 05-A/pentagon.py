def pentagon(n):  # n = 3 => 2, 5, 12
    for i in range(1, n+1):
        bilangan = int(i * (3*i-1) / 2)
        print(bilangan, end=" ")


# bagian utama
# input user
print('Deret n bilangan pentagon')
n = int(input('Masukkan n: '))
pentagon(n)
