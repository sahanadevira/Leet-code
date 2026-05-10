def maximum_jumps(nums, target):
    n = len(nums)
    # dp[i] stores the maximum jumps to reach index i
    dp = [-1] * n
    dp[0] = 0
    
    for j in range(1, n):
        for i in range(j):
            # Check if index i is reachable and jump condition is met
            if dp[i] != -1 and abs(nums[j] - nums[i]) <= target:
                dp[j] = max(dp[j], dp[i] + 1)
    
    return dp[n-1]

def main():
    print("--- Maximum Number of Jumps Calculator ---")
    try:
        # Get the array from the user
        raw_nums = input("Enter the numbers separated by spaces (e.g., 1 3 6 4 1 2): ")
        nums = [int(x) for x in raw_nums.split()]
        
        # Get the target value
        target = int(input("Enter the target value: "))
        
        if len(nums) < 2:
            print("Please enter at least two numbers.")
            return

        result = maximum_jumps(nums, target)
        
        if result == -1:
            print("\nResult: -1 (The last index is unreachable)")
        else:
            print(f"\nResult: {result} (Maximum jumps possible)")
            
    except ValueError:
        print("Invalid input. Please make sure to enter only integers.")

if __name__ == "__main__":
    main()
