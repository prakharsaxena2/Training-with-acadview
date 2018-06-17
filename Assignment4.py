tuple_1 = (1,2,3,34,'prakhar','hello','parth','kabir')     #create tuple
print(tuple_1)
l=len(tuple_1)                                              #calculate length of tuble
print("Length of tuple",l)

tuple_2 = (3,6,34,12,34,33,234,1221,1,0)
max = max(tuple_2)                  #calculate max in tuple
min = min(tuple_2)                  #calculate min in tuple
print("largest element",max)
print("smallest element",min)

tuple_3 = (1,2,3,4,5,6,7,8)

product = 1             #storage variable
for item in  tuple_3:               #calculate prduct of each element in tuple
    product = product * item
print(product)



a = set([1,2,3,4,0,23,13,15])   # set a

b = set([12,0,1,3,4,78,90,23])  #set  b
print(a-b)                      # difference in set

print(a&b)                      # intersection in set

                                 # different comparesion operations in set a and set b
print(a<b)

print(a>b)

print(a<=b)

print(a>=b)

print(a!=b)

            #directory  questions need help

spell = list('MISSISSIPPI')     # spell variable
print(spell)
print("Number of M",spell.count('M'))   #count no. of M
print("Number of I",spell.count('I'))   #count no. of I
print("Number of S",spell.count('S'))   #count no. of S
print("Number of P",spell.count('P'))   #count no. of P