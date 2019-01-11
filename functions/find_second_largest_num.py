nums = map(int, raw_input().split())
max1, max2 = float('-inf'), float('-inf')
for num in nums:
    if num > max2:
        if num > max1:
            max2, max1 = max1, num
    else:
        max2 = num
print max2



