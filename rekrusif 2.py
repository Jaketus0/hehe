def sum_looping(n): #1+2+3+4+...+n=?
    hasil= 0 
    for i in range(1, n+1): 
        hasil= hasil+i
    return hasil

def sum_rumus(n): #(1+n) * (n/2)
    return int ((1+n) * (n/2))

def sum_rekursif(n): 
    #base case 
    if n == 1: 
        return 1 
    else: 
        return sum_rekursif (n-1) + n
    
print(sum_looping(17))
print(sum_rumus(17))
print(sum_rekursif(17))