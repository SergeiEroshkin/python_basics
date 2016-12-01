num = int(raw_input())
nums = raw_input()
nums_list = list(set(nums.split(' ')))
print nums_list
n = max(nums_list)
print n
l = []
l = [nums_list[i] for i in range(len(nums_list)) if n != nums_list[i]]
print max(l)