def fibo(n):
    f1, f2 = 1, 1
    fib = 1
    for i in range(2,n):
        fib = f1+f2
        f1 = f2
        f2 = fib
    return fib 

def fibo_rekursif(n): 
    if n == 1 or n == 2: 
        return 1 
    else: 
        return fibo_rekursif(n-1) + fibo_rekursif(n-2)
    
def fibo_rekursif_memoization(n,list_fibo):  #supaya lebi cepet 
    if n == 1 or n == 2: 
        return 1 
    else: 
        if list_fibo[n-1] != 0:
            return list_fibo[n-1]
        else: 
            list_fibo[n-1] = fibo_rekursif_memoization(n-1, list_fibo) + \
                fibo_rekursif_memoization(n-2, list_fibo)
            return fibo_rekursif_memoization(n-1, list_fibo) + fibo_rekursif_memoization(n-2, list_fibo)
    
hasil = fibo(20)
print(f'Fibo perulangan: {hasil}')
    
hasil = fibo_rekursif(20)
print(f'Fibo rekursif: {hasil}')

n = 41
list_fibo= [0] * n
hasil= fibo_rekursif_memoization(n,list_fibo)
print(f'Fibo rekursif memoization: {hasil}')

