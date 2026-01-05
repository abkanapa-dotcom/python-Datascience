class Vehicle:
    def __init__(self):
        pass
    def Bike(self,bikename):
        self.bikename = bikename
        print(f"{self.bikename} in Base class")
    @classmethod
    def Car(self,carname):
        self.carname=carname
        print(f"{self.carname} in derived class")
obj_vehicle=Vehicle()
obj_vehicle=Vehicle().Bike("KTM")

# print(obj_vehicle.Car())
# print(Vehicle.Car())
# print(obj_vehicle.Bike())
# print(Vehicle().Bike())
print("###########################################################")
class Employee:
    # A class attribute, shared by all instances
    num_employees = 0

    def __init__(self, name):
        # An instance attribute, unique to each instance
        self.name = name
        Employee.num_employees += 1 # Update class attribute on new instance creation

    # An instance method: accesses instance data (self.name)
    def display_info(self):
        print(f"Employee Name: {self.name}") # Accesses instance data

    # A class method: accesses class data (cls.num_employees)
    @classmethod
    def display_count(cls):
        print(f"Total Employees: {cls.num_employees}") # Accesses class data

# Using the methods
emp1 = Employee("Alice")
emp2 = Employee("Bob")

emp1.display_info()     # Output: Employee Name: Alice
Employee.display_count() # Output: Total Employees: 2
Employee('Abhi').display_info()
emp1.display_count()


print("###########################################################")
class Employee:
    company = "TechCorp"   # class variable

    def __init__(self,name,salary, office):
        self.name = name          # instance variable
        self.salary = salary
        self.company=office
        print("line 55: ",Employee.company)
        print(f"{self.name} with {self.salary} working for {office}")
        return None

    def yearly_salary(self):      # instance method
        return self.salary * 12

    @classmethod
    def change_company(cls, new_company):   # class method
        cls.company = new_company
        print("Line 65: ",new_company)

    @staticmethod
    def is_high_salary(salary):    # static method
        return salary > 50000


# Exercise usage
e1 = Employee("Anu", 60000,'HCL')
e2 = Employee("Rahul", 40000,'wipro')

print(e1.name, e1.yearly_salary())
# print("High salary:", Employee.is_high_salary(e1.salary))

# Employee.change_company("NextGen Tech")
# print("Company:", Employee.company)

print("###########################################################")

