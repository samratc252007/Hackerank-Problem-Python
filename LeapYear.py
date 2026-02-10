def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 400 == 0):
        leap = True
    elif (year % 4 == 0 and year % 100 != 0):
        leap = True
        
    return leap

# The HackerRank environment will handle input and function calls.
# You just need to complete the function definition above.
# Example of how the function is used in the challenge:
# year = int(input())
# print(is_leap(year))
