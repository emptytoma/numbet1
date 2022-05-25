import random
 #1.0
print("Задание 1.0")
x1, y1, x2, y2 = random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10)
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
print(f'Расстояние между точками: {distance(x1, y1, x2, y2)}')

#1.1
print('_'*100 + "\n" "Задание 1.1")
dist_list = [] # создание списка

x1, y1, x2, y2, x3, y3 = random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10)
x1, y1, x2, y2, x3, y3 = float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)

first = distance(x1, y1, x2, y2)
second = distance(x2, y2, x3, y3)
therd = distance(x3, y3, x1, y1)

dist_list.append(distance(x1, y1, x2, y2))
dist_list.append(distance(x2, y2, x3, y3))
dist_list.append(distance(x3, y3, x1, y1))

print(dist_list)

#1.2
print('_'*100 + "\n" "Задание 1.2")
def square (numbers_list: list):
    
    a = numbers_list[0]
    b = numbers_list[1]
    c = numbers_list[2]
    if a + b > c and a + c > b and b + c > a:
        p = (numbers_list[0] + numbers_list[1] + numbers_list[2]) / 2
        return (p * (p - numbers_list[0])*(p - numbers_list[1])*(p - numbers_list[2]))**0.5
    else:
        return(-1)
    
#1.3

print('_'*100 + "\n" "Задание 1.3")
big_list = []
i = 0
list_input = str()
while i < 5:
    list_input = input(f"Введите 3 числа для подсписка {i}: ")
    list_input = list_input.split()
    list_input[0],list_input[1],list_input[2] = float(list_input[0]),float(list_input[1]),float(list_input[2]),
    big_list.append(list_input)
    i += 1
print(big_list) 

#1.4
print('_'*100 + "\n" "Задание 1.4")
j = 0
while j < 5:
    print( f'Площадь треугольника {square(big_list[j])}' )
    j += 1

