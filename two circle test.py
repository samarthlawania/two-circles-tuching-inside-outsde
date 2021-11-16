x1 = int(input("Enter the x-coordinate of bigger circle"))
y1 = int(input("Enter the y-coordinate of bigger circle"))
x2 = int(input("Enter the x-coordinate of smaller circle"))
y2 = int(input("Enter the y-coordinate of smaller circle"))
R = int(input("Enter the  radius of bigger circle"))
r = int(input("Enter the x-coordinate of smaller circle"))
D = ((x2-x1)**2 + (y2-y1)**2)**0.5
if D < R+r:
    print("Inside")
elif D == R + r:
    print("Touching")
else:
    print("Outside")
