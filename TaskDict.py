towns = {'city': 'Moscow', 'temperature': '20'}
print(towns.get('city'))

towns['temperature'] = int(towns['temperature'])-5 #Изменил строку на число
print(towns)

