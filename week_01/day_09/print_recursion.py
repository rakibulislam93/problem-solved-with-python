
# time and space complexity -----> O(n)
def print_recursion(n):
    if n==0:
        return 
    else:
        print('I love Recursion')
        print_recursion(n-1)
    
n = int(input())
print_recursion(n)