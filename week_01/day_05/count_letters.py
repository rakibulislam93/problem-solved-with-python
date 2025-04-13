
# time complexity -----> O(n)
# space complexity ----> O(n) because string er size = n hote pare 
S = input()
counter = {chr(i):0 for i in range(ord('a'),ord('z')+1)}

for char in S:
    counter[char] +=1
    
for key,value in counter.items():
    if value > 0:
        print(f'{key} - {value}')
    

