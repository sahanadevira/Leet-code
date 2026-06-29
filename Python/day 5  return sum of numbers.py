def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] == target - nums[i]:
                return [i, j]
    return []

# User Input
raw_input = input("Enter numbers: ")
numbers = [int(x) for x in raw_input.split()]
target_val = int(input("Enter target: "))

# Function Call
result = twoSum(numbers, target_val)
print("Result indices:", result)
