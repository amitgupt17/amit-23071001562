C1=complex(input("Enter first complex number = "))
C2=complex(input("Enter second complex number = "))
if C1.real>C2.real:
    print("The first complex number",C1,"has a greater real part")
elif C1.real<C2.real:
    print("The second complex number",C2,"has a greater real part")
else:
    print("both complex numbers have equal real part")