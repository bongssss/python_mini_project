import math


import math

def perfectSquare(x):
    square = math.sqrt(x)
    return square * square == x

def fibNo(n,):
    return perfectSquare(5*n*n + 4) or perfectSquare(5*n*n - 4) 
   

N = int(input('number: '))
def isFib(N):
    if fibNo(N) == True:
        return f' {N} is a fibonacci number'
    else:
        return f'{N} is not a fibonacci number'
    
print(isFib(N))

w = 1 +math.sqrt(5)
b = 1- math.sqrt(5)
print(w,b)

       


    

