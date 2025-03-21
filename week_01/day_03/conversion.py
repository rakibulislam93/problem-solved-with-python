
my_str = input()

my_list = list(my_str)

for index,value in enumerate(my_list):
    if value==',':
        my_list[index]=' '
    elif value>='a' and value<='z':
        my_list[index] = value.upper()
    elif value>='A' and value<='Z':
        my_list[index] = value.lower()

new_str = "".join(my_list)
print(new_str)

