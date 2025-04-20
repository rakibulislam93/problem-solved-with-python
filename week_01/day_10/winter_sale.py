
# time and space complexity ----- > O(1)
x,p = map(int,input().split())

original_price = ((p*100)/(100-x))
print(f'{original_price:.2f}')