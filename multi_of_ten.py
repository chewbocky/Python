number = input("please inputa number and I will tell you if it is a multiple of 10. ")
number = int(number)

if number %10 == 0:
	print(f"Number {number} is a multiple of 10")
else:
	print(f"Number {number} is not a multiple of 10.")