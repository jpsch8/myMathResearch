print("numeric integration")
a = float(input("lower bound_ "))
b = float(input("upper bound_ "))
fa = float(input("f(a)_ "))
fb = float(input("f(b)_ "))
point = (b-a)/6
mid = float(input("f("+str(point)+")_ "))
aprox = point*(fa+(4*point)+fb)
print("the area under the curve from x="+str(a)+" to x="+str(b)+ " is roughly " + str(aprox))
