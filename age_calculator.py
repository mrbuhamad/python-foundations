from datetime import date

def check_birthdate(year,month,day):
	birthday= date(year,month,day)
	check= birthday<=date.today()
	return check

def calculate_age(year,month,day):
	birthday= date(year,month,day)
	today=date.today()
	age=today.year-birthday.year

	print("You are " + str(age) + " years old.")
	

year_input= int(input("Enter year of birth:  "))
month_input= int(input("Enter month of birth:  "))
day_input= int(input("Enter day of birth:  "))

if check_birthdate(year_input,month_input,day_input)== True:
	print (calculate_age(year_input,month_input,day_input))
else:
	print("pleas inter a valid birthday")



