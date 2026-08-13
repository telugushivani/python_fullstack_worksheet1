class Student:
    def display_details(self):
        print(f"Name",self.name)
        print(f"Roll Number",self.roll_number)
        print(f"Marks",self.marks)
student1=Student()
student2=Student()
student3=Student()
student1.name="Rupa"
student1.roll_number=101
student1.marks=87
student1.display_details()
student2.name="Raju"
student2.roll_number=102
student2.marks=90
student2.display_details()
student3.name="shivani"
student3.roll_number=103
student3.marks=79
student3.display_details()
