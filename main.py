from problem_solving_one import problem_one, problem_three, problem_two

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

#Compress a string of characters
#Utilize a for loop and a counter with an if statement checking if the previous index is the same
#If it is then I will add to the counter until it isnt then we will concat the counter as well as the letter.
#Reset the counter and repeat. Also removing eacSh letter as we search for it

compress_send_data = "aaabbbbbccccddddeeeedda"
compress_return_data = problem_three(compress_send_data)
print(f"{compress_send_data} compressed down is, {compress_return_data}")