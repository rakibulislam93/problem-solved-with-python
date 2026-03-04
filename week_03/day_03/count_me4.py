
# freq = [0]*26
# s = input()
# for i in s:
#     freq[ord(i)-ord('a')] += 1

# for i in range(26):
#     if freq[i] > 0:
#         print(f"{chr(i+ord('a'))} - {freq[i]}")

freq = {chr(i):0 for i in range(ord('a'), ord('z')+1)}
s = input()
for i in s:
    if i in freq:
        freq[i] += 1

for i in freq:
    if freq[i] > 0:
        print(f"{i} - {freq[i]}")