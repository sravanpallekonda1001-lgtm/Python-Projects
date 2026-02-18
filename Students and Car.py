# Creating parametric class
class Students():
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course
        print(self.name,self.course,self.roll_no)
    def details(self):
        print("student name is:",self.name)
        print("student roll number:",self.roll_no)
        print("student enroling the course:",self.course)
     
#____________________________________________________________________
class Car():
    def __init__(self,Brand,Model,Color,Eng_Type):
        self.brand=Brand
        self.model=Model
        self.color=Color
        self.eng_type=Eng_Type
    def details(self):
        print("Car name is :",self.brand)
        print("model name is:",self.model)
        print("color name is",self.color)
        print("engine type is:",self.eng_type)