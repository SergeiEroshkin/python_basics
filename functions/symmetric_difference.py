m = int(raw_input())
m_num = set(map(int, raw_input().split()))
n = int(raw_input())
n_num = set(map(int, raw_input().split()))
dif = list((m_num.difference(n_num))) + list((n_num.difference(m_num)))
print '\n'.join(map(str, [i for i in sorted(dif)]))