import numbers
def return_value():
    print("this is a function")
    #return 1000

print(return_value())

def return_integer()->int:
    return 5
print(return_integer())


def cub(num:int)->int:
    return num*num*num

print(cub(5))

def add(num1:numbers,num2:numbers,num3:numbers=0,num4:numbers=0)->numbers:
    return num1+num2+num3+int(num4)
print(add(3,5))
print(add(3,4,6,7.7))