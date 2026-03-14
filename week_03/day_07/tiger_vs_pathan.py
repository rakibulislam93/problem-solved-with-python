
n = int(input())
s = input()

count_t = 0
count_p = 0
for char in s:
    if char == 't' or char == 'T':
        count_t += 1
    elif char == 'p' or char == 'P':
        count_p += 1

if count_t > count_p:
    print("Tiger")
elif count_p > count_t:
    print("Pathaan")
else:
    print("Draw")