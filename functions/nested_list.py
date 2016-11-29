N = int(raw_input())
final = list()
for i in range(N):
    lst = list()
    name = str(raw_input())
    marks = float(raw_input())
    lst.append(name)
    lst.append(marks)
    final.append(lst)
k = list()
for i in range(len(final)):
    k.append(final[i][1])
x = min(k)
k1 = list()
for i in range(len(k)):
    if x != k[i]:
        k1.append(k[i])
y = min(k1)
student = list()
for i in range(len(final)):
    if y == final[i][1]:
        student.append(final[i][0])
student.sort()
for i in range(len(student)):
    print student[i]