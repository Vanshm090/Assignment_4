import random

num1=random.randint(1,10)
num2=random.randint(1,10)

print(int(num1))
print(int(num2))

a=int(input("Give your answer"))

answer=int(num1*num2)

if a==answer:
    print("you are right")
else:
    print("you are wrong")