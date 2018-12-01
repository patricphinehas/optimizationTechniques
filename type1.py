#inputdata
cor = (input("enter the cordinates separated by comma"))
print(cor)
a,b= cor.split(",")

a = int(a)
b = int(b)

tol = int(input("enter the tollerance percentage in numerical"))

#formula for length
le = b - a


n = (le*100/tol)-1

pn = n/100

print(pn)

i=0
for i in range(0.01,5.00, pn):
    print(i)

import numpy as pynum
import math
#print("Printing floating-poinst range with numpy.arange() \n", pynum.arange(0, 5.5, 0.5), "\n")

c = pynum.arange(0.00,5.00, pn)

x=0
q=0
for x in pynum.nditer(c):
    print(x, "  ")
    if x!=0:
        print("value not found")
    else:
        q = 0.65-(0.75/(1+x**2))- 0.65 * (x) * (1/(math.tan(1/x)))
        print(x, "the value is",q)
    
