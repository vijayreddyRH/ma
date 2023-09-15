import math
# Parent class
class Shape:
 def __init__(self):
 pass
 def calculate_area(self):
 pass
# Child class - Triangle inherits from Shape
class Triangle(Shape):
 def __init__(self, base, height):
 super().__init__()
 self.base = base
 self.height = height
 
 def calculate_area(self):
 return 0.5 * self.base * self.height
# Child class - Circle inherits from Shape
class Circle(Shape):
 def __init__(self, radius):
 super().__init__()
 self.radius = radius
 
 def calculate_area(self):
 return math.pi * self.radius**2
# Child class - Rectangle inherits from Shape
class Rectangle(Shape):
 def __init__(self, length, width):
 super().__init__()
 self.length = length
 self.width = width
 def calculate_area(self):
 return self.length * self.width
# Creating instances of each class
triangle = Triangle(5, 7)
circle = Circle(3)
rectangle = Rectangle(4, 6)
# Calculating and printing the area of each shape
print("Area of Triangle:", triangle.calculate_area())
print("Area of Circle:", circle.calculate_area())
print("Area of Rectangle:", rectangle.calculate_area())



####################################3


class Employee:
 def __init__(self, name, employee_id, department, salary):
 self.name = name
 self.employee_id = employee_id
 self.department = department
 self.salary = salary
 def update_salary(self, new_salary, department):
 if self.department == department:
 self.salary = new_salary
 def __str__(self):
 return f"Name: {self.name}\nEmployee_ID: {self.employee_id}\nDepartment: 
{self.department}\nSalary: {self.salary}"
# Create employees
employee1 = Employee("John Doe", 1, "Finance", 5000)
employee2 = Employee("Jane Smith", 2, "Engineering", 6000)
employee3 = Employee("Tom Wilson", 3, "Engineering", 5500)
# Print employee details before updating salary
print("Before salary update:")
print(employee1)
print(employee2)
print(employee3)
# Update salary of employees belonging to "Engineering" department
new_salary = 6500
department = "Engineering"
employee2.update_salary(new_salary, department)
employee3.update_salary(new_salary, department)
# Print employee details after updating salary
print("\nAfter salary update:")
print(employee1)
print(employee2)
print(employee3)
