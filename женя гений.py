import random
 #1.0
#print("Задание 1.0")
x1, y1, x2, y2 = random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10)
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
print(f'Расстояние между точками: {distance(x1, y1, x2, y2)}')
dist_list = []
#1.1
# print('_'*100 + "\n" "Задание 1.1")
# dist_list = [] # создание списка
def coordinates():
    
    x1, y1, x2, y2, x3, y3 = random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10)
    x1, y1, x2, y2, x3, y3 = float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)

    first = distance(x1, y1, x2, y2)
    second = distance(x2, y2, x3, y3)
    therd = distance(x3, y3, x1, y1)

    dist_list.append(distance(x1, y1, x2, y2))
    dist_list.append(distance(x2, y2, x3, y3))
    dist_list.append(distance(x3, y3, x1, y1))
    
    return dist_list

#print(dist_list)

#1.2
# print('_'*100 + "\n" "Задание 1.2")
swar = [8, 9, 55]
def square (numbers_list: list):
    
    a = numbers_list[0]
    b = numbers_list[1]
    c = numbers_list[2]
    if a + b > c and a + c > b and b + c > a:
        p = (numbers_list[0] + numbers_list[1] + numbers_list[2]) / 2
        return   (p * (p - numbers_list[0])*(p - numbers_list[1])*(p - numbers_list[2]))**0.5
    else:
        return(-1)
print(f"{square(swar)}")    
#1.3

# print('_'*100 + "\n" "Задание 1.3")
big_list = []
# list_input = str()
for i in range(1):
    big_list.append(coordinates())
print(big_list)
for triangle in big_list:
    ploshad_trianle = square(triangle)
    if ploshad_trianle < 0:
        print("Треугольник не существует")
    else:
        print(ploshad_trianle)
    # list_input = input(f"Введите 3 числа для подсписка {i}: ")
    # list_input = list_input.split()
    # list_input[0],list_input[1],list_input[2] = float(list_input[0]),float(list_input[1]),float(list_input[2]),
    # big_list.append(list_input)
    


#1.4
# print('_'*100 + "\n" "Задание 1.4")

# for j in range(5):
#     print( f'Площадь треугольника {square(big_list[j])}' )
    
# #2.0
# print('_'*100 + "\n" "Задание 2.0")

dist_list.sort()
a = dist_list[0]
b = dist_list[1]
c = dist_list[2]

if a**2 + b**2 == c**2:
    print("треугольник прямоугольный")
    print(square(triangle))
else:
    print("net")
