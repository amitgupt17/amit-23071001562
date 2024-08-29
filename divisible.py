num=int(input("Enter the number = "))
if num==0:
    print("Number is zero and not divisible by both 2 and 8")
elif num<0:
    print(num,"is negative and can't be divisible by both 2 and 8")
elif num%2==0 and num%8==0:
    print(num,"is divisible by both 2 and 8")
else:
    print(num,"is not divisible by both 2 and 8")

output
Enter the number = 45
45 is not divisible by both 2 and 8
