def format_price(price): #Задал функцию
  price = int(price) #Обозначил, что моё число может быть только целым
  return 'Цена:' + str(price) + 'руб' #Результатом функции должно быть СТРОЧНОЕ зачение
l = format_price(56.24) #Задаём произвольное значение агрумента
print(l)