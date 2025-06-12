###  create list
fruits=["banana","apple","orange"]
fruits.append("cherry")
print(fruits[-1])
fruits.insert(1,"mango")
print(fruits)
fruits.remove("banana")
popup=fruits.pop()
print(fruits)
del fruits[0]
print(fruits)
if "apple" in fruits:
    print("apple is there")


print("-----------string review-----------------------")
n="Automation testing"
print(n[:7])
print(n[-1])
print(n[1:])
print(n[:1])
print(n[len(n)-1])
n=n.lower()
print(n)
reversed_n=n[::-1]
print(reversed_n)
print(n[0:-1])
print(n[::-1])
n=n[:10]
print(n[::-1])
reversed_str2=reversed(n)
print(type(reversed_str2))
print("".join(reversed_str2))
