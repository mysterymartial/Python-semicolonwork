def reversed(number):
	reverse = 0
	while number > 0:
		reverse = reverse * 10 + (number%10)
		number = number // 10
		
	return reverse



def palindrome(number):

	original_number = number
	reverse = 0
	while number > 0:
		reverse = reverse * 10 + (number%10)
		number = number // 10
		if number == reverse:
			return f"your number is palindrome"
		else:
			return f"your number is not a palindrome"


	
number = int(input("Enter set of whole numbers \n"))
result = reversed(number)
result1 = palindrome(number)
print(result)
print(result1)