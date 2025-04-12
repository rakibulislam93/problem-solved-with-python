
t = int(input())

for i in range(t):
    s = input()
    # capital,small,digit=0,0,0
    # for char in s:
    #     if char>='A' and char<='Z':
    #         capital += 1
    #     elif char>='a' and char<='z':
    #         small += 1
    #     else:
    #         digit += 1
    
    capital = sum(1 for char in s if char.isupper())
    small = sum(1 for char in s if char.islower())
    digit = sum(1 for char in s if char.isdigit())

    print(capital,small,digit)