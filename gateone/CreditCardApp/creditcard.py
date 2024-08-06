def first_step(card_number):
	total = 0
	sum =0 
	for count in range(0,len(card_number),2):
		numbers = int(card_number[count])
		numbers = (numbers * 2)
		if numbers >=10:
			first_digit = numbers % 10
			second_digit = numbers // 10
			sum = first_digit + second_digit
			total = total + sum
		else:

			total += numbers
		
	return total

	
def second_step(card_number):
	sum = 0
	for counter in range(0,len(card_number),1):

		numbers = int(card_number[counter])
		if numbers % 2 != 0:
			sum += numbers


	return sum
			
		
		
		
		
		
