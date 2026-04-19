import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

no_of_letters=int(input("How many letters would you like in your password? "))
no_of_symbols=int(input("How many symbols would you like? "))
no_of_numbers=int(input("How many numbers would you like? "))

final_password=""
pass_list=[]

for i in range(no_of_letters):
    pass_list.append(random.choice(letters))
for i in range(no_of_symbols):
    pass_list.append(random.choice(symbols))
for i in range(no_of_numbers):
    pass_list.append(random.choice(numbers))
random.shuffle(pass_list)
for letter in pass_list:
    final_password+=letter

print(final_password)
