import sys 
sys. setrecursionlimit(10000)

# def hello_world(n):
#     for i in range(n):
#         print('Hello world')
# hello_world(10)

def hello_world_rekursif(n): #max cuma bisa 1000 
    if n == 0:
        return #exit dari fungsi
    else:
        print(f'Hello world {n}') #print sekali
        hello_world_rekursif(n-1) #sisanya
hello_world_rekursif(10)

def hello_world_rekursif(n): #max cuma bisa 1000 
    if n == 0:
        return #exit dari fungsi
    else:
        print('Hello world') #print sekali
        hello_world_rekursif(n-1) #sisanya
        print(f'{n}') #print sekali
hello_world_rekursif(10)
