

browser_name = "fire_fox"

if browser_name == "chrome":
    print("Chrome Browser is selected")
    print("Opening Chrome Browser")
elif browser_name == "fire_fox":
    print("Fire_fox Browser is selected")
    print("Opening fire_fox Browser")
else:
    print("Safari Browser is selected")
    print("Opening safari Browser")

    print("-----------------------------------------")

score = -200
if 0 <= score <= 100:
    if score >= 60:
        print("passed")
    else:
        print("failed")
else:
    print("invalid")

    #### int=input()
    ### print("hello "+ int)

    print("-----------------------------------------")

temperature = 25
if temperature > 30:
    print("it is hot")
elif temperature > 20:
    print("it is warm")
else:
    print("it is cool")

for i in range(5):
    print(i)
for j in range(0, 10, 2):
    print(j)
names=["Bob","James","Nancy"]

for name in names:
    print(name)

count=0
while count<3:
    print(f"count:{count}")
    count+=1

for i in range(10):
    if i==3:
        continue
    if i==7:
        break
    print(i)

s="selenium"
revers_str=""
for i in s[::-1]:
  revers_str+=i

print(revers_str)