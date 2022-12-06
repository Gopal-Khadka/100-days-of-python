from math import ceil
test_h=int(input("Enter the height of the wall:\n"))
test_w=int(input("Enter the width of the wall:\n"))
coverage=5

def paint_calc(height,width):
	no_of_cans=ceil(height * width / coverage)
	print(f"The no of cans of paint required is : {no_of_cans}")

paint_calc(height=test_h,width=test_w)