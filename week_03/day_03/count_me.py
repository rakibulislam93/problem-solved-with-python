
n = int(input("Enter a number: "))
arr = list(map(int, input().split()))
dividor_two = 0
dividor_three = 0
for i in arr:
    if i % 2 == 0:
        dividor_two += 1
    elif i % 3 == 0:
        dividor_three += 1
    
    elif i % 2 == 0 and i % 3 == 0:
        dividor_two += 1

print("Divisor of 2:", dividor_two)
print("Divisor of 3:", dividor_three)