my_dict = {'city1': {'city': 'Appletown', 'population': 1324, 'asl': True},
           'city2': {'city': 'Banana Height', 'population': 324, 'asl': True},
           'city3': {'city': 'Cherry Grove', 'population': 324, 'asl': False}
           }


# Return Name of city with largest name
def largest_city(dictionary):
    if len(dictionary['city1']['city']) > len(dictionary['city2']['city']) and len(dictionary['city1']['city']) > len(dictionary['city3']['city']):
        return dictionary['city1']['city']
    if len(dictionary['city1']['city']) < len(dictionary['city2']['city']) or len(dictionary['city1']['city']) < len(dictionary['city3']['city']):
        if len(dictionary['city2']['city']) > len(dictionary['city3']['city']):
            return dictionary['city2']['city']
        else:
            return dictionary['city3']['city']


# Return population of cities stored in dictionary
def cities_population(dictionary):
    return dictionary['city1']['population'] + dictionary['city2']['population'] + dictionary['city3']['population']


# Return city(cities)with smallest population
def lowest_population(dictionary):
    if dictionary['city1']['population'] < dictionary['city2']['population'] and dictionary['city1']['population'] < dictionary['city3']['population']:
        return dictionary['city1']['population']
    if dictionary['city1']['population'] == dictionary['city2']['population'] and dictionary['city1']['population'] < dictionary['city3']['population']:
        return dictionary['city1']['city'], dictionary['city2']['city']
    if dictionary['city1']['population'] == dictionary['city3']['population'] and dictionary['city1']['population'] < dictionary['city2']['population']:
        return dictionary['city1']['city'], dictionary['city3']['city']
    if dictionary['city1']['population'] > dictionary['city2']['population'] or dictionary['city1']['population'] > dictionary['city3']['population']:
        if dictionary['city2']['population'] == dictionary['city3']['population']:
            return dictionary['city2']['city'], dictionary['city3']['city']
        elif dictionary['city2']['population'] < dictionary['city3']['population']:
            return dictionary['city2']['city']
        else:
            return dictionary['city3']['city']


def main():
    print largest_city(my_dict)
    print cities_population(my_dict)
    print lowest_population(my_dict)


if __name__ == '__main__':
    main()
