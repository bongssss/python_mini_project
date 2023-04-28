import math


import math

def perfectSquare(x):
    square = int(math.sqrt(x))
    return int(square * square) == x

def fibNo(n,):
    return perfectSquare(5*n*n + 4) or perfectSquare(5*n*n - 4) 
   

N = int(input('number: '))
def isFib(N):
    if N == 0 or N == 1 or N == 2 or N ==3:
        return f' {N} is a fibonacci number'
    if fibNo(N) == True:
        return f' {N} is a fibonacci number'
    else:
        return f'{N} is not a fibonacci number'
    
print(isFib(N))

w = 1 +math.sqrt(5)
b =  math.sqrt(5) - 1
print(w,b)

       


    

