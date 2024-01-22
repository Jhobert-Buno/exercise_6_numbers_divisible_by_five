# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# pseudocode
# create functions
def divfive (numbers):
    for divisible_by_five in numbers:
        if divisible_by_five % 5 == 0:
            print(divisible_by_five)

print("EXAMPLE")
# given list of nubers
given_list = [10, 20, 33, 46, 55]

# print the result
print("The given numbers are: ", given_list)
print("Numbers divisible by five: ")
divfive(given_list)

print(" ")
# ask user to input numbers
print("Please Input Five Numbers:", )
num1=int(input("1st number: "))
num2=int(input("2nd number: "))
num3=int(input("3rd number: "))
num4=int(input("4th number: "))
num5=int(input("5th number: "))

input_numbers = [num1,num2,num3,num4,num5]
print("The numbers are: ", input_numbers)
print("Numbers divisible by five: ")
divfive(input_numbers)