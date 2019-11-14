city_dict = {'Moscow': {'population': 1000, 'Subway': True},
             'EKB': {'population': 300,'Subway': False},
             'SPB': {'population': 200, 'Subway': True},
             'Chekhov': {'population': 250, 'Subway': False}}


def get_values(dictionary):
    for key, value in dictionary.iteritems():
        if dictionary[key].values()[0] is False:
            print dictionary[key].values()
            print 'City without Subway is {0}.'.format(key)


get_values(city_dict)


