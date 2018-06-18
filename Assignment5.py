year = input("Enter the years")
y=int(year)             #convert string to int
print(year)

if y%400==0:
    print("leap year")
elif y%100==0:
    print("Not leap year")
elif y%4==0:
    print("leap year")
else:
    print("Not leap year")

length = input("Enter length ")
breadth =input("Enter the breadth")
l=float(length)
b=float(breadth)    #convert string to float
if l==b:
    print("Dimension of square");
else:
    print("Dimensions of rectangle")

p1 = input("Age of person 1")
p2 = input("Age of person 2")
p3 = input("Age of person 3")

x = int(p1)         #convert string to int
y = int(p2)         #convert string to int
z = int(p3)         #convert string to int


print(x,y,z)
if (x>y) and (x>z):
    print("p1 is oldest")
elif (y>x) and (y>z):
    print("p2 is older")
else:
    print("p3 is oldest")

if (x<y) and (x<z):
     print("p1 is youngest")
elif (y<x) and (y<z):
       print("p2 is youngest")
else:
    print("p3 is youngest")


points = input("Enter the point")
p_s = int(points)           #convert string to int
if p_s>=1 and p_s<=50:
    print(" No prize ")
elif p_s>=51 and p_s<=150:
    print("Congratulations! -- Wooden Dod")
elif p_s>=151 and p_s<=180:
    print("Congratulations! -- Book")
elif p_s>=181 and p_s<=200:
    print("Congratulations! -- Chocolates")
else:
    print("Sorry! No prize this time")





quantity = input("Enter the quantity")
q = int(quantity)       #convert string to int
s = q*100

l = int(s)              #convert string to int
if l>=1000:
    print("total cost",l-(10*l)/100)
else:
    print("No discount")
