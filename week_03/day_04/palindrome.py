
s = input()

# def is_palindrome(s:str)->bool:

#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# if is_palindrome(s):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

def is_palindrome(s:str)->bool:
    return s == s[::-1]

print("Palindrome" if is_palindrome(s) else "Not Palindrome")