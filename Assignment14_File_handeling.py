'''Q1'''
'''Defining function to read line from last'''
def read_last_lines(filename, lines):
    with open(filename, "r") as text_file:
        '''opening file in read mode'''
        contents = text_file.readlines()[-lines:]
        '''read lines from last'''
        for line in contents:
            print(line, end="")
            '''printig lines'''

'''Main program'''
n = int(input("Enter the Number of lines to be read: "))
'''Taking number of lines from user'''
read_last_lines("abc.txt", n)
'''Calling funtion to print those lines'''
'''Q.2'''
num_words = 0
with open("abc.txt",'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

print("Number of words:",num_words)

'''Q.3'''
f = open("abc.txt",'r')
f1 = open("xyz.txt",'w')
f1.writelines(f.readlines())
f.close()
f1.close()

'''Q4'''
with open('abc.txt') as fh1, open('xyz.txt') as fh2:
    '''Opening assingent.txt as fh1 and new.txt as fh2'''
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)
        '''printing corresponding lines from both files'''

'''Q5'''

import random

with open('number.txt','w') as fin:
    for i in range(1,11):
        '''Writing Random numbers in num.txt'''
        l = random.randint(0,999)
        fin.write(str(l) + "\n")
fin.close()

li = []

with open("number.txt","r") as fout:
    for line in fout:
        li.append(int(line))
    li.sort()

with open("sorted.txt", "w") as fsort:
    for i in range(0,10):
        fsort.write(str(li[i]) + "\n")
fout.close()

fsort.close()
