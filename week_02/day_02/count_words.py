
# time and space complexity ----> O(n)
# code runtimes = 10^6 / 10^7
# code take memory = 10^6 * 1bytes / 1000 = 1000 kb /1000= 1 + extra 5Mb

s = input()

puntuations = ['!','.','?',',']

for p in puntuations:
    s = s.replace(p,' ')

newstring = s.split()
count = 0
for word in newstring:
    if word.isalpha():
        count +=1
    
print(count)