from bs4 import BeautifulSoup
import requests 

              #Defining companyes url
companyes=[
{"name":"NBK", "url":'https://english.mubasher.info/markets/BK/stocks/NBK/profile'},
{"name":"OOREDOO","url":"https://english.mubasher.info/markets/BK/stocks/OOREDOO/profile"},
{"name":"ZAIN","url":"https://english.mubasher.info/markets/BK/stocks/ZAIN/profile"},
{"name":"JAZEERA","url":"https://english.mubasher.info/markets/BK/stocks/JAZEERA/profile"},
{"name":"ALRAI","url":"https://english.mubasher.info/markets/BK/stocks/ALRAI"}]


def chosen_company(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	                  # accessing company_name#
	company_name=stock_price = soup.find_all(class_="mi-section__title")[0].get_text()
	print("------------------------------------------")
	print(f"\n -- {company_name} --\n")
	print("------------------------------------------")
	                   # accessing Stock Price#
	stock_price = soup.find_all(class_="market-summary__last-price")[0].get_text()
	print(f"\n    Current Stock price: {stock_price}")
                       # accessing market_volum#
	market_volum=soup.find_all(class_="market-summary__block-number")[4].get_text()
	print(f"\n    Stock Volum: {market_volum}")
                       # accessing market_turnover#
	market_turnover=soup.find_all(class_="market-summary__block-number")[5].get_text()
	print(f"\n    Stock Turnover: {market_turnover}")

	print("------------------------------------------")


user_input=""
while user_input!=str(0) and user_input.upper()!="LEAVE":
	print ("")
	print ("\n Welcom To my simple stock information platform\n")
	print ( "   Pleas Choose one of the following companies  ")
	x=0

	#       printintg the list of companyes
	for items in companyes:
		x=x+1
		com_name=items["name"]
		print( f"    {x} - {com_name}")

	print ("\n     print 0 or \"leave\" to Exit \n")


	user_input=input("   which company would you like to choose?  ")
	print("")



	if user_input==str(0) or user_input.upper()=="LEAVE":
		break
	else:
		if user_input.isdigit()==False or int(user_input) > 5:
			print("------------------------------------------")
			print("     your input is invaled pleas try again")
			print("------------------------------------------")
		else:
			chosen_company(companyes[int(user_input)-1]["url"])





