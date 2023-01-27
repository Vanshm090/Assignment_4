a=int(input("Enter the year"))

if a%400==0:
    print("This is a leap year")
elif a%100==0:
    print("this is not a leap year")

elif a%4==0:
    print("this is a leap yaer")

else:
    print("this is not a leap year")