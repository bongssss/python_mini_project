import math as m  
   
# Here, we will create a utility function that will return true if K is a perfect square  
def is_Perfect_Square(K):  
    s = int(m.sqrt(K))  
    return s * s == K  
   
# Now, we will create a function which will return "true" if R is a Fibinacci Number,   
# else it will return "false"  
def is_Fibonacci(R):  
   
    # R is a Fibinacci number only if one of (5 * R * R + 4) or (5 * R * R - 4) or both   
   # of them are perferct square  
    return is_Perfect_Square(5 * R * R + 4) or is_Perfect_Square(5 * R * R - 4)  
      
# Now, we will create a utility function for testing the above functions 
n = int(input('number: ')) 
def fib(n): 
     
    if (is_Fibonacci(n) == True):  
         print ("Number:", n, ": Yes, the given number is a Fibonacci Number")  
    else:  
         print ("Number:", n, ": No, the given number is not a Fibonacci Number")  
    return n

print(fib(n))


w = 1 +m.sqrt(5)
b = 1- m.sqrt(5)
print(w,b)
