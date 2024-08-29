present_year=int(input("Enter the present year = "))
birth_year=int(input("Enter the birth year = "))
age=present_year-birth_year
if age>=18:
    print("You can vote and Age is",age)
elif age<18:
    print("You cannot vote after",age,"year for wait but you can vote now this year is",birth_year+18)

output
Enter the present year = 2024
Enter the birth year = 1989
You can vote and Age is 35
again
Enter the present year = 2024
Enter the birth year = 2009
You cannot vote after 15 year for wait but you can vote now this year is 2027
