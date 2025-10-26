name = input(str("Enter your first name and last name with space: "))
first_name, last_name = name.split(" ")
reversed_name = last_name + " " + first_name
print("Reversed name is: " + reversed_name)