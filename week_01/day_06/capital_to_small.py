
def capital_to_small(char):
    return chr(ord(char)+32)

value = input()[0]
print(capital_to_small(value))