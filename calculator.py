frstNum=  int(input("Enter the first number  "))
scnDNumb=  int(input("Enter the second number  "))
opration= input ("Choose the operation (+, -, /, *)  ")
answer=0
if opration== "+":
	  answer= frstNum + scnDNumb
elif opration== "-":
	  answer= frstNum - scnDNumb
elif opration== "/":
	  answer= frstNum / scnDNumb
elif opration== "*":
	  answer= frstNum * scnDNumb
else:
	  answer= ("Error Choose the opertion (+, -, /, *)")
print ("the answer is  "+ str(answer))