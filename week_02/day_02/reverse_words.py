
# time complexity -----> O(n)
s = input()

newstring = s.split()

for i,word in enumerate(newstring):
    result = ''.join(reversed(word))
    
    if i!=len(newstring)-1:
        print(result,end=' ')
    else:
        print(result)

