def rotate_string(s: str, goal: str) -> bool:
    if len(s) != len(goal):
            return False
    length  = len(s) 

    for i in range(length):
        s = s[1:] + s[0]
        if s == goal:
            return True
    return False
    


    
s = input("Enter string s: ")
goal = input("Enter string goal: ")
    
    
result = rotate_string(s, goal)
print(f"Result: {result}")
    
        
