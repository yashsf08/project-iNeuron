"""
2. Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
"""

first_name = input("Dear User, Please provide your Full Name : ")
print("Name in Reverse Order: ", first_name[::-1])
name = first_name.split()
print("Another Type of reverse order ", ' '.join(name[::-1]))
