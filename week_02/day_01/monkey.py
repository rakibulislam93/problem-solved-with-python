
try:
    while True:
        s = input()
        print(''.join(sorted(char for char in s if char != ' ')))

except EOFError:
    pass