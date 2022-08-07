from problem_solving_one import problem_one, problem_two

#Reverse a string
#I will be utilizing a function from problem_solving_one.py
#It will utilize the string inputted
#Ex word[::-1]
#This starts at the beginning of any sized string, ends at any sized string and increments -1 causing the string to be reversed

reverse_send_data = input("Please input a sentence. ")
reverse_return_data = problem_one(reverse_send_data)
print(f"{reverse_send_data} reversed is, {reverse_return_data}")

#Capitalize letter
#My thought process is to take a sentence, seperate it into a list based on the spaces, then use the title method to capitalize and input into a string.

capitalize_send_data = input("Please input a sentence. ")
capitalize_return_data = problem_two(capitalize_send_data)
print(f"{capitalize_send_data} capitalized is, {capitalize_return_data}")

