#Вывести максимальное из двух введенных чисел. 

def task_max(x, y):
    if x > y:
        print(x)
    elif y > x:
        print(y)
    else:
        print(y)

task_max(999,137)


#Вывести "yes", если произвольные числа различаются на 135 и "no" в остальных случаях
#Как взять модуль - честно выяснено в интернетах, иначе мне короткого пути не придумалось.

def task_135 (x, y):
    if abs (x - y) == 135:
        print('yes')
    else:
        print('no')

task_135(2, 137)


#По номеру месяца определить сезон года
#Насчет in range - я не вспомнила, где это было. просто срисовала с упражнения в уроке.
#Т.к. номера только целые, я решила, что надо ограничить тип данных

def season (s: int):
    if s == 12 or s == 1 or s == 2:
        print('зима')
    elif s in range (3, 6):
        print('весна')
    elif s > 5 and s < 9:
        print('лето')
    elif 9 <= s <= 11:
        print('осень')
    else:
        print('введены неверные данные')
    
season(10)


#Если 3 произвольных числа больше 10, то "yes", в остальных случаях - "no"

def num_10 (x, y, z):
    if x > 10 and y > 10 and z > 10:
        print('yes')
    else:
        print('no')

num_10(11,55,-500)


#Из списка из 5 чисел найти количество положительных

def task_list (a5: list):
    print(sum(1 for a in a5 if a > 0))

task_list([1, 2, -3, 4, -5])

#Посчитать количество дней, при введенном кол-ве лет и месяцев. В месяце 29 дней.

def days(year: int, month: int):
    print(year*12*29 + month*29)

days(15, 3)

