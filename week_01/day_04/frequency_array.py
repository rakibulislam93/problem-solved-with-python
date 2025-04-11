
#input n and m
n,m = map(int,input().split())

# set 0 from 1 to m..
m_counter = {i:0 for i in range(1,m+1)}

arr = list(map(int,input().split()))

# increase key value
for val in arr:
    m_counter[val]+=1

for key,value in m_counter.items():
    print(value)

