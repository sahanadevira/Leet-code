def is_valid_array(nums):
    n = len(nums)         
    count = [0] * n         
    for a in nums:             
        if a >= n:                 
            return False             
        if a < n - 1 and count[a] > 0:                 
            return False             
        if a == n - 1 and count[a] > 1:                 
            return False             
        count[a] += 1         
    return True
