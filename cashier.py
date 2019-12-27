item_input=""
price_input=""
quantity_input=""
order={}
orders_list=[]
#defining names 

while item_input != "done":
	item_input=input ("Item (enter \"done\" when finished):  ")
	if item_input == "done":
		break
		#this line to prevent the loop to cont. 
	price_input=float(input("Price:  "))
	quantity_input=int(input("quantity:  "))

	order={"name":item_input,"price":price_input,"quantity":quantity_input}
	orders_list.append(order)
	#creating a list of dictionares for each item

print()
print()
print("---------------")
print("Receipt")
print("---------------")

total_recipt_price=0
for items in orders_list:
	Receipt=items 
	#making each dictionary as single itration and naming it receipt
	item_total_price=Receipt["price"]*Receipt["quantity"]
	total_recipt_price+=item_total_price
	print("%s %s %sKD" %(Receipt["quantity"],Receipt["name"],round(item_total_price,4)))

print("---------------")

print("Total Price: %sKD" %(round(total_recipt_price,4)))