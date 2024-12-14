# Input 
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Dictionary to store the count of multiples for numbers 1 to 9
multiples_count = {}

# Loop 
for i in range(1, 10):  
    # Count how many num in the list are div by 'i'
    count = 0
    
    # Check & Increment
    for num in numbers:
        if num % i == 0: 
            count += 1 

    # Store  in dictionary
    multiples_count[i] = count

# Print result
print(multiples_count)
