class Employee:
    def __init__(self,employee_id,employee_name,salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.salary=salary
    def display_details(self):
      print(f"Employee Id",self.employee_id)
      print(f"Employee Name",self.employee_name)
      print(f"salay",self.salary)

emp=Employee(101,"Rupa",20000)
emp1=Employee(102,"Ajay",50000)
emp2=Employee(103,"Pavani",30000)
emp.display_details()
emp1.display_details()
emp2.display_details()
