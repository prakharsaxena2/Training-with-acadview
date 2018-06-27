class Animal:
   legs = 4
   eyes = 2

   def walk(self):
       print("Animal with %d legs" %self.legs)

   def see(self):
       print("Animal is seeing with %d eyes" %self.eyes)


class Tiger(Animal):
    legs = 4
    eyes = 8

animal = Animal()
animal.walk()
animal.see()

tiger = Tiger()
tiger.walk()
tiger.see()

# A A

class Cops:
   c_name = "Singhum"
   c_age = 44
   c_work_experience = 23
   c_designation = "Inspector"
   def add(self):
       self.c_name = input("Enter the name")

       self.c_age = int(input("Enter the age"))

       self.c_work_experience = input("Enter work experience")

       self.c_designation = input("Enter designation")

   def display(self):
       print(self.c_name)
       print(self.c_age)
       print(self.c_work_experience)
       print(self.c_designation)

   def update(self):
       self.c_name = input("Enter the name")

       self.c_age = input("Enter the age")

       self.c_work_experience = input("Enter work experiencde")

       self.c_designation = input("Enter designation")


class Mission(Cops):
    def add_mission(self,newcop = Cops()):
        newcop.add()
        newcop.display()
        newcop.update()

newMission = Mission()
newMission.add_mission()


###################
class Shape:
    length = 0
    breadth = 0
    def area(self):
        area = self.length*self.breadth
        print("Area",area)

class Rectangle(Shape):
    length = 3
    breadth = 4
class Square(Shape):
    length = 4
    breadth = 4

shape = Shape()
shape.area()
rectangle = Rectangle()
rectangle.area()
square = Square()
square.area()
