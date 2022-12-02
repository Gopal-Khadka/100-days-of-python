import random

testSeed=input("Enter any seed number :")
random.seed(testSeed)

#primary method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
number= len(names)
nameNo=random.randint(0,number-1)
print(nameNo)
print(names[nameNo] + " is going to pay the bill.")

#secondary method
person_to_pay  = random.choice(names)
print(person_to_pay + " is going to pay the bill.")