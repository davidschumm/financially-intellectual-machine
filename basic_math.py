
import robin_stocks as rs
from datetime import date 

today = date.today()

prim_bank = {'checking_acct' : {"amount" : 2101.12}, 'savings_acct' : {"amount" : 5.01}}

stocks = {"Robinhood" : {"amount": 2836.92}, "TDAmeritrade": {"amount": 610.12}, "Webull": {"amount": 1911.34}}
crypto = {"Coinbase": {"amount":791.98}, "Cashapp" : {"amount":1471}} 

debt = {'student loans': {"amount": 200}, 'credit cards': {"amount": 0}}

food = {'Groceries':{'amount':63}, 'Restaurants':{'amount':70}}
travel = {'Gas':{'amount':60}, 'Flights':{'amount':300}}
housing = {'Rent':{'amount':550}, 'Utilies':{'amount':70}}
ecommerce = {'Amazon':{'amount':200}, 'Etsy': {'amount':15}}


username =  'davidschumm'
password = 'Das200351455'
rs.robinhood.authentication.login(username=username,
		password=password,
		expiresIn=86400,
		by_sms=True)

robin_user = rs.robinhood.profiles.load_account_profile()

print(robin_user)

rs.robinhood.authentication.logout()

def add_up_cat(categ):

	sumed = 0
	for acct in categ.values():
		sumed += sum(acct.values())
	return sumed

sumbank = add_up_cat(prim_bank)
sumstonk = add_up_cat(stocks)
sumcryp = add_up_cat(crypto)
totalasset = sumbank+sumbank+sumcryp

sumdebt = add_up_cat(debt)
sumfood = add_up_cat(food)
sumtrav = add_up_cat(travel)
sumhous = add_up_cat(housing)
sumecom = add_up_cat(ecommerce)
totalliab = sumdebt+sumfood+sumtrav+sumhous+sumecom

def get_percentages(cat, typeof):
	if typeof == "Assets":
		senten = "of total Assets"
		denom = totalasset
		percent =(cat / denom)*100
		return str(percent) + "% " + senten

	elif typeof == "Liabilities":
		senten = "of Total Liabilities"
		denom = totalliab
		percent = (cat / denom)*100
		return str(percent) +"% " + senten	
	else:
		return "Invalid Category"


def call_percent(catword):
	if catword == "Bank Account":
		return catword + " is " + get_percentages(sumbank, "Assets")
	elif catword == "Stocks":
		return catword + " are " + get_percentages(sumstonk, "Assets")
	elif catword == "Crypto Currencies":
		return catword + " are " + get_percentages(sumcryp, "Assets")
	elif catword == "Debts":
		return catword + " are " + get_percentages(sumdebt, "Liabilities")
	elif catword == "Food":
		return catword + " is " + get_percentages(sumfood, "Liabilities")
	elif catword == "Travel":
		return catword + " is " + get_percentages(sumtrav, "Liabilities")
	elif catword == "Housing":
		return catword + " is " + get_percentages(sumhous, "Liabilities")	
	elif catword == "Ecommerce":
		return catword + " is " + get_percentages(sumecom, "Liabilities")	
	
def total_networth(assets, liabil):
	networth = assets - liabil
	return "Current Net Worth is " + str(networth) + "!"
'''
print(networth)

print("assets", assets)
print("bank", bank)
print("stock", sumstonk)
print("crypt", sumcryp)
print("debtdic", sumdebt)
'''

#print(bankper)
print(call_percent("Bank Account"))
print(call_percent("Stocks"))
print(call_percent("Crypto Currencies"))

#####

######### Expenses ##########
# Monthly # write formula to convert to daily, etc
print(call_percent("Debts"))
print(call_percent("Food"))
print(call_percent("Travel"))
print(call_percent("Housing"))
print(call_percent("Ecommerce"))

print(total_networth(totalasset, totalliab))