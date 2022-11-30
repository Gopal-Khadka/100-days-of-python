#sum digits of two digit number

#other way
twoDigitNumber = input("Enter a two digit number: ")

Firstdigit = twoDigitNumber[0]
secondDigit = twoDigitNumber[1]

sumof = int(Firstdigit) + int(secondDigit)

print("Sum of the digits of number is \n",sumof)

#my way|
Twodigitno = input("Enter a two Digit Number : ")
first_digit = int(Twodigitno)%10
second_Digit = int(int(Twodigitno)/10) #division gives us float numbers
result = first_digit + second_Digit
print(result)
