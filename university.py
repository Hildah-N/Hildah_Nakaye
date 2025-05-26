#parent
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

   #sub class :Student     
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def info(self):
        super().info()
        print(f"Student ID: {self.student_id}")

# sub class :Lecturer
class Lecturer(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def info(self):
        super().info()
        print(f"Employee ID: {self.employee_id}")     

# sub class :Staff
class Staff(Person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self.staff_id = staff_id

    def info(self):
        super().info()
        print(f"Staff ID: {self.staff_id}")        

        #create objects of each class
student = Student("Alice", 20, "S12345")
lecturer = Lecturer("Dr. Smith", 45, "E67890")
staff = Staff("Bob", 35, "T54321")

# Display information for each person
student.info()
lecturer.info()
staff.info()