
# time and space comlexity -----> O(n)
def print_number(n):
    if n==0:
        return
    else:
        print_number(n-1)
        # print(n)
        return n

n = int(input())
print(print_number(n))