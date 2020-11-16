# Gather general details about the property:
location = input("what is the address of this property? ")
price = int(input("What is the asking price? "))
rent = int(input("What is the expected rent per month? "))
prop_tax = int(input("What is the estimated property tax (per year)? "))
print("1. Percentage")
print("2. Specific Amount")
down_type = float(input("Do you want to enter a percentage or specific amount? "))

# Figure out the down payment amount:
downpayment = int(0)
if down_type == 1:
	percent_down = input("Please enter the precentage: ")
	percent_down = float(percent_down) / 100
	downpayment = int(price * percent_down)
elif down_type == 2:
	specific_down = int(input("Please enter the specific value: "))
	downpayment = down_type
else:
	print("Please select a valid option.")
	quit()
# Figure out the loan terms:
years = int(input("What is the length of the loan? "))
interest_rate = float(input("Current interest rate for the loan: "))
interest_rate = interest_rate / 100
gross_rent = rent * 12

principal = price - downpayment
#print(principal)
mortgage_payment = (principal * (interest_rate * ((1 + interest_rate) ** years)) / ((1 + interest_rate) ** years - 1)) / 12
#print(mortgage_payment)

# General expenses to calculate:
repairs = gross_rent * .10
cap_ex = gross_rent * .10
vacancy = gross_rent * .08

# Need to validate the cash flow and cap rate to help determine the value of the deal:
cash_flow = (gross_rent - (mortgage_payment + repairs + cap_ex + vacancy + prop_tax)) / 12
cap_rate = (gross_rent / price) * 100

# Calculate the minimum amount of cash needed to close on the deal, this includes the "sales tax" of 2.5% and agent fees:
cash_required = downpayment + (price * .025) + (price * .03)

# To verify what is considered a "great/good/bad" deal based on the estimated cap rate:
analyzer = None
if cap_rate >= 10:
	analyzer = "this is a great deal!"
elif cap_rate >= 7:
	analyzer = "this is a good deal."
else:
	analyzer = "this is a bad deal."

# Send all this data to a text file for review later:
f = open("Rentals.txt", "a")
with open("Rentals.txt", "a") as f:
	print("=========================", file=f)
	print("Address:", location, file=f)
	print("Asking Price:", price, file=f)
	print("Rent:", rent, file=f)
	print("Gross Rent per Year:", gross_rent, file=f)
	print("Estimated Property Tax: ", prop_tax, file=f)
	print("Repairs: ", repairs, file=f)
	print("Cap Ex: ", cap_ex, file=f)
	print("Vacancy: ", vacancy, file=f)
	print("The estimated cash flow per month is: $", int(cash_flow), "with a cap rate of:", round(cap_rate, 2), "%", file=f)
	print("With this estimated cap rate,", analyzer, file=f)
	print("The minimum cash required (includes down payment and closing costs) is: $", cash_required, file=f)
	f.close()










