def get_summ(one, two, delimiter='&'):  #Задал функцию
  return str(one) + ' ' + delimiter + ' ' + str(two) #Передаю в функцию строчное значение
  
print(get_summ(1, 2)) #Выводим функцию с произвольными аргументами






def l_p(name1,name2):  #Задал функцию
   return name1 +' '+ name2 #Передаём сумму агрументов

lp = l_p('Learn', 'python') #Вводим переменную lp
print(lp)  

LP = str(lp).upper() #Вводим переменную LP с перобразованной в строку lp для возможности вывода заглавными буквами с помощью команды >upper()<
print(LP)