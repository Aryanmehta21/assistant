print("Enter a number!")
n1 = float(input())
print("Enter 2nd number!")
n2 = float(input())
print("Enter the operator---->+,-,*,/,%")
op = input()
print("\n")


if '+' in op:
    print("The result is:",n1+n2)

elif '-' in op:
    print("The result is:",n1-n2)

elif '*' in op:
    print("The result is:",n1*n2)

elif '/' in op:
    print("The result is:",n1/n2)
elif '%' in op:
    print("The result is:",n1%n2) #for knowing the remainder!!