# candies=int(input("no of candies"))

# for candies in range (1,200):
#     if (candies%5 ==2):
#         continue
#     if(candies%6 ==3):
#         continue
#     if(candies%7==2):
#         continue   
# print(candies , "is the answer")
#     break
    
n=int(input("enter no of candies"))

for n in range(1,n+1):
    if n%5==2 and n%6==3 and n%7==2:
        print(n)
                         

        








