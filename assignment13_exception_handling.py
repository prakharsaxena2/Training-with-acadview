
'''Q1'''
'''ZeroDivisonError'''

a=3
if a<4:
    try:
        a=a/(a-3)
        print(a)
        '''Try function'''
    except ZeroDivisionError:
        print("Division by Zero not possible")
        '''Exception Handelled'''

'''Q2'''
'''IndexError'''
try:
    l=[1,2,3]
    print(l[3])
    '''Try function'''
except IndexError:
    print("List Index is out of range. Ramge is 0-2")
    '''Exception Handelled'''

'''Q3'''
'''
An exception
Traceback (most recent call last):
  File "*Path of program*", line 4, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there
'''

'''Q4'''
'''
-5.0
a/b result in 0
'''

'''Q5'''
'''1'''
try:
    print(time.ctime())
except :
    print("time module is not imported")

'''2'''
try:
    x = int(input("Enter a number"))
except ValueError:
    print("Only an Integer has to be entered")

'''3'''
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("List Index is out of range. Ramge is 0-2")

'''Q6'''
'''Define Exception'''
class AgeTooSmallError(Exception):
    pass

'''Main Program starts'''
while True:
    try:
        age = int(input("Enter age: "))
        if age < 18:
            raise AgeTooSmallError
        break
    except AgeTooSmallError:
        print("Age should be more than 18")
    except ValueError:
print("Age should be a number")