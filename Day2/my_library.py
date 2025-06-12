import numbers


def add(num1:numbers,num2:numbers,num3:numbers=0,num4:numbers=0)->numbers:
    return num1+num2+num3+int(num4)

def cub(num:int)->int:
    return num*num*num