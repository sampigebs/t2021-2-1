# input from the user
a = int(input("Enter a number: "))

# Initialize an empty list to store the odd numbers
odd_numbers = []

# Generate odd numbers
for i in range(1, a*2, 2):  
    odd_numbers.append(i)

# Print the generated odd numbers
print(*odd_numbers, sep=", ")
