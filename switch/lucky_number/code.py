# Get the person's name as input
name = input("Enter your name: ")

# Calculate the number of letters in the name
name_length = len(name)

# Initialize a variable to store the lucky number
lucky_number = None

# Assign a number based on the length of the name
while lucky_number is None:
    if name_length == 0:
        lucky_number = 0
    elif name_length == 1:
        lucky_number = 1
    else:
        lucky_number = name_length

# Print the lucky number
print(f"Your lucky number is {lucky_number}.")
