
# time complexity ----> O(n log n)
n = int(input())
s = input()

count = [0]*26

for char in s:
    count[ord(char)-ord('a')]+=1

for i in range(26):
    print(chr(i+ord('a')) * count[i] , end='')

# count = {chr(ch):0 for ch in range(ord('a'),ord('z'))}
# for char in s:
#     count[char] += 1

# for key,value in count.items():
    
#     if value>0:
#         print(key*value,end='')
