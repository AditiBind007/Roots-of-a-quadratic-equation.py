a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
d = b*b - 4*a*c
if d<0:
    print("Roots are imaginary and unequal.")
else:
    if d == 0:
        print("Roots are real and equal.")
        x = -b/(2*a)
        print(f"X = {x}")
    else:
        print("Roots are real and unequal.")
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        print(f"X1 = {x1} and X2 = {x2}")
