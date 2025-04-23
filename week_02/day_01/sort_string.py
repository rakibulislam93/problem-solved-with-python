
# time complexity ----> O(n log n)
n = int(input())
s = input()

count = {chr(ch):0 for ch in range(ord('a'),ord('z'))}
for char in s:
    count[char] += 1

for key,value in count.items():
    
    if value>0:
        print(key*value,end='')
