
t = int(input())

for _ in range(t):
    first_farmer,last_farmer,days = map(int,input().split())

    work_days = (first_farmer*days)//(first_farmer+last_farmer)

    few_days = days - work_days

    print(few_days)

