num = int(raw_input())
heights = map(int, raw_input().split())
average = sum(set(heights)) / float(len(set(heights)))
print average