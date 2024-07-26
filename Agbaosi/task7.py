# prompt user for final account value
# prompt user for monthly_interest_rate
# prompt user for number of month
# divide final account value with 1 + monthly intresrt rate raised to pow number of month
# print the output as intial deposit

def intial_deposit(final_account_value,monthly_intrest_rate,numbers_of_month):

		deposit = (final_account_value / 1 + monthly_interest_rate) ** numbers_of_month
		
		return deposit




		
final_account_value = float(input("Enter your final account value \n"))
monthly_interest_rate = int(input("Enter your monthly interest rate \n"))
numbers_of_month = int(input("Enter number of month \n"))
result = intial_deposit(final_account_value, monthly_interest_rate, numbers_of_month)
print(f"your intial deposit is {round(result,1)}")



	
