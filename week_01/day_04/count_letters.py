
alpha_dic = {chr(i):0 for i in range(ord('a'),ord('z')+1)}

arr = input()

for char in arr:
    alpha_dic[char]+=1

for key,value in alpha_dic.items():
    if value>0:
        print(f'{key} : {value}')
