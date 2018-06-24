class Circle:                       #Q.1
    def __init__(self, radius):
        self.radius = radius
    def get_Area(self):
        area = 3.14*self.radius*self.radius
        print("Area of circle = ",area)
    def get_Circumference(self):
        circumference = 2*3.14*self.radius
        print("Circumference of circle = ", circumference)
r = int(input("Enter the radius "))
obj = Circle(r)
obj.get_Area()
obj.get_Circumference()

class Student:                      #Q.2
    def __init__(self, name ,roll_number):
        self.name = name
        self.roll_number = roll_number
    def Display(self):
        print("Name : ",self.name)
        print("Roll Number : ",self.roll_number)

name = input("Enter the name ")
roll_number = input("Enter the roll number")
obj = Student(name,roll_number)
obj.Display()

class Temp:                         #Q.3
    def __init__(self,temp):
        self.temp = temp
    def convert_cal_to_fah(self):
        fahrenheit = self.temp*1.8+32
        return fahrenheit
    def convert_fah_to_cal(self):
        calsius = (self.temp - 32)/1.8
        return  calsius

temp = int(input("Enter the temperature"))
print("Enter  1  to calsius to fahrenhiet")
print("Enter  2  to fahrenhiet to calsius")
n = int(input())
obj = Temp(temp)
if n==1:
    print("fahrenhiet = ",obj.convert_cal_to_fah())
else:
    print("calsius = ",obj.convert_fah_to_cal())


class Movie:                        #Q.4
    def __init__(self, movie_name = 'Sanju', artist_name = 'Ranbir kapoor', year_release = "26/June/2018", rating = 5):
        self.movie_name = movie_name
        self.artist_name = artist_name
        self.year_release = year_release
        self.rating = rating

    def Display(self):
        print("Movie name = ",self.movie_name)
        print("Artist Name = ",self.artist_name)
        print("Year of release = ",self.year_release)
        print("Rating = ", self.rating)
    def Update(self):
        self.movie_name = input("Enter movie of update")
        self.artist_name = input("Enter artist to update")
        self.year_release = input("Enter year_release")
        self.rating = int(input("Enter rating to update"))

obj = Movie()
obj.Display()
obj.Update()
obj.Display()

class Expenditure:              #Q.5
    def __init__(self,expenditure, saving, salary = 0):
        self.expenditure = expenditure
        self.saving = saving
        self.salary = salary
    def Display(self):
        print("Expenditure = ",self.expenditure)
        print("Saving = ",self.saving)
    def Calculate(self):
        self.salary = self.expenditure + self.saving
    def Display_salary(self):
        print("Total Salary = ",self.salary)
exp = int(input("Enter the expenditure"))
sav = int(input("Enter the saving"))
obj = Expenditure(exp,sav)
obj.Display()
obj.Calculate()
obj.Display_salary()
