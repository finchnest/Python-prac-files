import math
print("Enter the coefficients in your quadratic expression respectively!")
def rootFinder(a,b,c):
    interior=b**2-4*a*c
    if interior>0:
        root1= (-b+ (math.sqrt(b**2-4*a*c)))/(2*a)
        root2=(-b- (math.sqrt(b**2-4*a*c)))/(2*a)
        print("The quadratic expression has 2 real roots and they are ", root1," and ", root2)
    elif interior==0:
        root1= (-b+ (math.sqrt(b**2-4*a*c)))/(2*a)
        root2=(-b- (math.sqrt(b**2-4*a*c)))/(2*a)
        print("Your quadratic expression has 1 real root and that is ", -b/2*a)
    else:
         print("Your quadratic expression has no real roots")

