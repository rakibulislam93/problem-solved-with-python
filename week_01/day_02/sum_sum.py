
n = int(input())
numbers = list(map(int,input().split()))


# using for loop..
# sum1 = 0;
# sum2 = 0;

# for i in range(n):
#     if numbers[i]>=0:
#         sum1+=numbers[i]
#     else:
#         sum2+= numbers[i]

#using list comprehension..

sum1 = sum(numbers[i] for i in range(n) if numbers[i]>=0)
sum2 = sum(numbers[i] for i in range(n) if numbers[i]<0)


print(sum1,sum2)