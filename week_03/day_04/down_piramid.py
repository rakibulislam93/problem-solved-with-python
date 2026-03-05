
n = int(input())
# space = 0
# star = 2*n - 1

# for i in range(1, n + 1):
#     for j in range(1, space + 1):
#         print(" ", end="")
#     for k in range(1, star + 1):
#         print("*", end="")
#     print()
#     space += 1
#     star -= 2

for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    
    for k in range(2*i-1):
        print("*", end="")
    print()