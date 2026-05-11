def separate_digits(nums):
    res = []
    for x in nums:
        tmp = []
        # Edge case: if the number is 0
        if x == 0:
            res.append(0)
            continue
            
        # Extract digits mathematically
        while x > 0:
            tmp.append(x % 10)
            x //= 10
        
        # Reverse the extracted digits and add to result
        res.extend(tmp[::-1])
    return res

# --- User Interaction Logic ---

# Get input from the user
user_input = input("Enter numbers separated by spaces (e.g., 13 25 8): ")

try:
    # Convert input string into a list of integers
    numbers = [int(n) for n in user_input.split()]

    # Call the function
    result = separate_digits(numbers)

    # Display the output
    print("Separated digits:", result)

except ValueError:
    print("Error: Please make sure you only enter whole numbers.")
