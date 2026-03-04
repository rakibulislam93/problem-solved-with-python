

# t = int(input())
# for _ in range(t):
#     s = input()
#     small = 0
#     capital = 0
#     digit = 0
#     for i in s:
#         if i.islower():
#             small += 1
#         elif i.isupper():
#             capital += 1
#         elif i.isdigit():
#             digit += 1

#     print(capital,small,digit)

t = int(input())
for _ in range(t):
    s = input()
    small = sum(c.islower() for c in s)
    capital = sum(c.isupper() for c in s)
    digit = sum(c.isdigit() for c in s)
    print(capital,small,digit)