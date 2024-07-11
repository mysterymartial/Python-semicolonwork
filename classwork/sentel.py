print("Welcome to The Mysterious Bank of Africa")
sentinel = "D"

alphabet = ""
balance = 0



while alphabet != sentinel:
	      
	alphabet =  input("Enter A to deposit B to withdrwal C to check balance and D to terminate\n")

	match (alphabet):
	

		case 'A':
			deposit = int (input("Enter the amount you want to deposit\n"))
			balance = balance + deposit

		case 'B':

			withdraw = int (input("Enter the amount you want to withdrwal\n"))
			balance = balance  - withdraw

		case 'C':
                  	  print("Your balance is ",  balance)

		
		


 