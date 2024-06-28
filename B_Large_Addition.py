# t = int(input())
# for _ in range(t):
#     s = input()
#     v = True

#     if s[0]!= '1':
#         v = False
#     else:
#         for i, c in enumerate(s[1:]):
#             if i!= len(s) - 2:
#                 if c == '0':
#                     v = False
#                     break
#             else:
#                 if c > '8':
#                     v = False
#                     break

#     if v:
#         print("YES")
#     else:
#         print("NO")

# t = int(input())
# for _ in range(t):
#     s = input()
#     if all(c != '0' for i, c in enumerate(s[1:-1])) and s[-1] <= '8' and s[0] == '1':
#         print("YES")
#     else:
#         print("NO")
t = int(input())  # Number of test cases

for _ in range(t):
    s = input().strip()  # Read each test case input
    
    char_count = {}  # Dictionary to store character counts
    
    # Populate dictionary with character counts
    for char in s[1:-1]:  # Exclude first and last characters
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Check conditions using dictionary approach
    if all(count > 0 for count in char_count.values()) and s[-1] <= '8' and s[0] == '1':
        print("YES")
    else:
        print("NO")


# Read the number of test cases
# num_test_cases = int(input())

# # Process each test case
# for _ in range(num_test_cases):
#     string = input()
    
#     first_char_is_one = (string[0] == '1')
#     all_non_zero = all(char != '0' for char in string[1:-1])
#     last_char_is_not_nine_or_more = (string[-1] <= '8')
    
#     if first_char_is_one and all_non_zero and last_char_is_not_nine_or_more:
#         print("YES")
#     else:
#         print("NO")
# Read the number of test cases

# Read the number of test cases
# num_cases = int(input())

# Process each test case
# for _ in range(num_cases):
#     # Read the input string for the current test case
#     number_str = input()
    
#     # Check if the first character is '1'
#     is_first_char_one = number_str[0] == '1'
    
#     # Check if all characters except the first and the last one are not '0'
#     no_zeros_in_middle = True
#     for idx in range(1, len(number_str) - 1):
#         if number_str[idx] == '0':
#             no_zeros_in_middle = False
#             break
    
#     # Check if the last character is less than or equal to '8'
#     is_last_char_valid = number_str[-1] <= '8'
    
#     # Determine the output based on the checks
#     if is_first_char_one and no_zeros_in_middle and is_last_char_valid:
#         print("YES")
#     else:
#         print("NO")


