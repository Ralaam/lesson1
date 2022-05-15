from itertools import product
from pprint import pprint


towns = {'city': 'Moscow', 'temperature': '20'}
print(towns.get('country'))
towns['country'] = 'Russia'
towns['date'] = '27.05.2019'
pprint(towns)
print(len(towns))