def circle(r):
    print("Area of circle",3.14*r*r)            #Q.1

radius = float(input("enter the radius of circle"))
circle(radius)

def perfect():                          #Q.2
    for i in range(1,1000):
        c = 0
        for j in range(1,i):
            if i%j==0 :
                c =  c + j
        if i==c:
            print("perfect number",i)

perfect()


def table(num,i):               #Q.3
    if i > 10:
        return 0
    else:
        print(num,"*",i,"=",num*i)
        return table(num,i+1)

number = int(input("Enter the any number or 12"))
table(number,1)


def power(a,b):             Q.4
    if b==0:
        return 1
    else:
        return (a*power(a,b-1))

a = int(input("Enter the value a"))
b = int(input("Enter the value of b"))
print("a^b = ",power(a,b))



def fact(num,list):         Q.5
    if num==0:
        return 1
    else:
        list.append(num)
        print(list)
        return num*fact(num-1,list)

list = []
number = int(input("Enter the number"))
print(fact(number,list))