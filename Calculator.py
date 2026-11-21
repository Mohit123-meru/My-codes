def sub ( a , b):
        minus = a - b
        print(minus)
        return (minus)

def add ( c, d):
        sums = c + d
        print(sums)
        return(sums)

def multiply ( e, f):
        product = e * f
        print(product)
        return (product)

def divide ( g, h):
        quotient = g / h
        print(quotient)
        return (quotient)

try:
    num = int(input("Enter a number ( 1 and beyond ) : "))
    
    nums = int(input("Enter a second number ( 1 and beyond ) : "))

    print (divide (num, nums))
    
    print ( multiply(num, nums))
    
    print (sub (num, nums))

    print (add (num, nums))

    print ("La la la la la!")
except ValueError :

    print ("Enter a nummber.")

except ZeroDivisionError :

    print("You should not enter a zero.")