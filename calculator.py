print("welcome to Era's Calculator")

print("1. integer value")
print("2. float value")
c=int(input())
print("you have entered type as:",c)
if c==1:
    x1=int(input("enter first number:"))
    x2=int(input("enter second number:"))
else:
    x1=float(input("enter first number:"))
    x2=float(input("enter second number:"))
    
def addition(x1,x2):
    return(x1+x2)
    
def subtraction(x1,x2):
    return(x1-x2)

def mul(x1,x2):
    return(x1*x2)

def division(x1,x2):
    return(x1/x2)
print("which operation do you want to perform:")
print("1. addition")
print("2. subtraction")
print("3. mul")
print("4. division")
c1=int(input())

if c1==1:
    print("the sum is:",addition(x1,x2))
elif c1==2:
    print("the sub of is:",subtraction(x1,x2))
elif c1==3:
    print("the product is:",mul(x1,x2))
else :
    print("the remainder is:",division(x1,x2))







#print(addition(x1,x2))
