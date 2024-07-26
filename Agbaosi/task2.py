#prompt the user to collect height in feet
# store it in a varriable
# divide the collected data by final varriable 0.305
# put the output in a varriable
# print the varriable

def height_converter(height_in_feet):

	height_in_meter = height_in_feet / 0.305
	return height_in_meter



height = float(input("Enter your height in feet \n"))
result = height_converter(height)
print("your height in meter is ", round(result, 3))

	

	