from datetime import date

print("\nWelcome to HR Pro 2020\n")

company_employee =[]
company_manager=[]



class Employee:
		def __init__(self,name,age,salary,employment_year):
			self.name=name
			self.age=age
			self.salary=salary
			self.employment_year=employment_year
		def get_working_years(self):
			working_years= date.today().year-int(self.employment_year)
			return working_years
		def __str__(self):
			return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}"

class Manager(Employee):
		def __init__(self,name,age,salary,employment_year,bonus_percentage):
			Employee.__init__(self,name,age,salary,employment_year)
			self.bonus_percentage=bonus_percentage
		def get_bonus(self):
			bonus= float(self.bonus_percentage)*float(self.salary)
			return bonus
		def __str__(self):
			return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}, {self.get_bonus()}"


user_input= 0
while user_input != 5:

	print("\nOptions:")
	print("   1. Show Employees")
	print("   2. Show Managers")
	print("   3. Add An Employee")
	print("   4. Add A Manager")
	print("   5. Exit\n")
	

	user_input= int(input ("What would you like to do?  " ))
	print("----------------")

	if user_input==1:
		print("Employees\n")
		for employee in company_employee:
			print (employee)
		print("----------------")

	elif user_input==2:
		print("Managers\n")
		for manager in company_manager:
			print (manager)
		print("----------------")

	elif user_input==3:
		
		name= input ("Name:  ")
		age= input ("Age: ")
		salary= input ("Salary: ")
		employment_year= input ("Employement Year: ")
		employee_object=Employee(name,age,salary,employment_year)
		company_employee.append(employee_object)
		print("Employee added succesfully\n")
		print("----------------")

	elif user_input==4:
		name= input ("Name:  ")
		age= input ("Age: ")
		salary= input ("Salary: ")
		employment_year= input ("Employement Year: ")
		bonus_percentage= input("Bonus Percentage: ")
		maneger_object=Manager(name,age,salary,employment_year,bonus_percentage)
		company_manager.append(maneger_object)
		print("Manager added succesfully\n")
		print("----------------")
		
	





	
		
		
