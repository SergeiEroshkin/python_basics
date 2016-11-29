num = int(raw_input())
nums = raw_input()
nums_list = nums.split(' ')
print nums_list
n = max(nums_list)
print n
l = []
for i in range(len(nums_list)):
    if n != nums_list[i]:
            l.append(nums_list[i])
print max(l)
