class Pupil:
    name = "Immah"
    age = 19
    school = "AkiraChix"
    country = "Kenya"



class Student():
    school = "AkiraChix"
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.year = 2025 - age
        self.marks= []


    def greet_student(self):
        print(f"Hello {self.first_name}, welcome to {self.school}")

    def initials(self):
        print(self.first_name[0],self.last_name[0])

    def total_marks(self, points):
        self.marks.append(points)
        total = 0
        for point in self.marks:
            total += point
            return total



    # def record_marks(self,marks):
    #     total_marks = sum(marks)
    #     print(f"Marks recorded: Total marks is {total_marks}")

         

# s1 = Student("Asha", "Meaza", 20, "Ethiopia")
# print(s1.first_name)
# print(s1.last_name)
# print(s1.age)
# s1.greet_student()
# s1.initials()
# s1.record_marks([55,68,68,90])

# s2 =Student("Alma", "Moores", 19, "Kenya")
# print(s2.first_name)
# print(s2.last_name)
# print(s2.age)
# s2.greet_student()
# s2.initials()
# s2.record_marks([90,56,78])