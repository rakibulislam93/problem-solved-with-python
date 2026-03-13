
n = int(input())
lucky_numbers = list(map(int, input().split()))
min_number = float('inf')
frequency = {}

for num in lucky_numbers:
    frequency[num] = frequency.get(num, 0) + 1
    if num < min_number:
        min_number = num


if frequency[min_number] % 2 == 1:
    print("Lucky")
else:
    print("Unlucky")