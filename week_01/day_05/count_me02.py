
# time complexity ---> O(n)
# space complexity ----> O(1)
S = input()
vowel,consonent = 0,0

for char in S:
    # if char == 'a' or char =='e' or char=='i' or char=='o' or char=='u':
    #     vowel += 1
    # else:
    #     consonent += 1
    
    if char in 'aeiou':
        vowel += 1
    else:
        consonent += 1

print(consonent)