i = 0               #Q.1
list_1 =[]
for i in range(10):
     number = int(input())
     list_1.append(number)

print(list_1)

j = 0
list_2 = [1,2,3,4]      #Q.2
for j in list_2:
    print(i)
    list_2.append(i)

list_3 = []
n = int(input("Enter the number of element"))
k = 0
for k in range(n):                  #Q.3
    num = int(input())
    list_3.append(num)


list_4 = []
for item in list_3:
    list_4.append(item*item)

print(list_4)


list_5 = [1,'prakhar','kk',5.6,'akshat','rajesh',3,4,5,9.7,66.9]        #Q.4
list_int = []
list_string = []
list_float = []
for item in list_5:
    if isinstance(item,int):
        list_int.append(item)
    elif isinstance(item,str):
        list_string.append(item)
    elif isinstance(item,float):
        list_float.append(item)


print("lsit containing",list_int)
print("list containing ",list_float)
print("lsit containing string",list_string)


list_even = []                          #Q.5
list_odd = []
i = 1
for i in range(101):
    if i%2==0:
        list_even.append(i)
    else:
        list_odd.append(i)

    i = i+1

print("Number of even list",list_even)
print("Number of odd list",list_odd)

for c in range(0,4):            #Q.6
    for j in range(0, c+1):
        print("*",end="")
    print("\r")

for x in range(3):          #Q.7
   people_dictionary = {}
   new_key = input('Enter new key: ')
   new_age = input('Enter new age: ')
   people_dictionary[new_key] = new_age
print(people_dictionary)



list_6 = []                 #Q.8
n = int(input("Emter the range"))
for i in range(n):
    list_6.append(int(input()))

num = int(input("Enter the number to be deleted"))
for i in list_6:
    if i==num:
        list_6.remove(num)

print(list_6)