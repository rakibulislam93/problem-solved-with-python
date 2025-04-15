
# time complexity ----> O(n)
# space complexity -----> O(n)
# def number_print(n):
#     mylist = []
#     for i in range(1,n+1):
#         mylist.append(i)
    
#     return mylist

# n = int(input())
# result = number_print(n)
# print(*result)

# optimize space complexity
def number_print(n):
    for i in range(1,n+1):
        if i==n:
            print(i)
        else:
            print(i,end=' ')

n = int(input())
number_print(n)