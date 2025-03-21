
# s1 = input()
# s2 = input()

# s1_list = list(s1)
# s2_list = list(s2)
# temp = s1_list[0]
# s1_list[0] = s2_list[0]
# s2_list[0] = temp

# print(len(s1),len(s2))
# print(s1+s2)
# print("".join(s1_list),"".join(s2_list))

s1 = input()
s2 = input()

# Print the lengths
print(len(s1), len(s2))

# Print the concatenated string
print(s1 + s2)

# Swap first characters and print modified strings
print(s2[0] + s1[1:], s1[0] + s2[1:])
