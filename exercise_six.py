# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# pseudocode
# create functions
def divfive (numbers):
    for divisible_by_five in numbers:
        if divisible_by_five % 5 == 0:
            print(divisible_by_five)

# given list of nubers
given_list = [10, 20, 33, 46, 55]

# print the result
print("The given numbers are: ", given_list)
print("Numbers divisible by five: ")
divfive(given_list)

