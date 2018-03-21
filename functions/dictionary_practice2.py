my_dict = {
    'Moscow': {'population': 100, 'Subway': True},
    'SPB': {'population': 50, 'Subway': True},
    'EKB': {'population': 30, 'Subway': False, }}

for k, v in my_dict.iteritems():
    if k == 'Moscow':
        print k, v