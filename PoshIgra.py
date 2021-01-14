# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import os.path

player1_name = input("Введирте имя игрока 1: ")
player2_name = input("Введирте имя игрока 2: ")
player1 = {
    'name': player1_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}
player2 = {
    'name': player2_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

if os.path.exists(f"{player1['name']}.txt") == False:
    player1_file = open(f"{player1['name']}.txt", 'w')
    for element in player1:
        player1_file.write(f'{element}: {player1[element]}\n')
    player1_file.close()

if os.path.exists(f"{player2['name']}.txt") == False:
    player2_file = open(f"{player2['name']}.txt", 'w')
    for element in player2:
        player2_file.write(f'{element}: {player2[element]}\n')
    player2_file.close()

def res_dam_arm(damage, armor):
    return round((float(damage)/float(armor)), 2)

def attack_vz(atacked_person, protecting_person):      # При взаимных ударах
    print(f'Игрок {atacked_person["name"]} атакует игрока {protecting_person["name"]} и наносит ему \033[31m{atacked_person["damage"]}\033[0m единиц урона, оставляя игроку {protecting_person["name"]} \033[31m{round((protecting_person["health"] - res_dam_arm(atacked_person["damage"], protecting_person["armor"])),2)}\033[0m жизней.\nЗащищаясь, {protecting_person["name"]} нанес в ответ игроку {atacked_person["name"]} \033[31m{protecting_person["damage"]}\033[0m урона, оставив ему \033[31m{round((atacked_person["health"] - res_dam_arm(protecting_person["damage"], atacked_person["armor"])),2)}\033[0m жизней.')
    protecting_person["health"] = round((protecting_person["health"] - res_dam_arm(atacked_person["damage"], protecting_person["armor"])), 2)
    atacked_person['health'] = round((atacked_person["health"] - res_dam_arm(protecting_person["damage"], atacked_person["armor"])), 2)
    if atacked_person["health"] <= 0 and protecting_person["health"] <= 0:
        print(f"\033[31mПобедителей нет...\033[0m")
    elif atacked_person["health"] <= 0:
        print(f"Игрок {atacked_person['name']} погибает, побеждает игрок {protecting_person['name']} с \033[31m{protecting_person['health']}\033[0m")
    elif protecting_person["health"] <= 0:
        print(f"Игрок {protecting_person['name']} погибает, побеждает игрок {atacked_person['name']} с \033[31m{atacked_person['health']}\033[0m")

def attack_odn(atacked_person, protecting_person):      # При одностороннем ударе
    print(f'Игрок {atacked_person["name"]} атакует игрока {protecting_person["name"]} и наносит ему \033[31m{atacked_person["damage"]}\033[0m единиц урона, оставляя игроку {protecting_person["name"]} \033[31m{round((protecting_person["health"] - res_dam_arm(atacked_person["damage"], protecting_person["armor"])),2)}\033[0m жизней.')
    protecting_person["health"] = round((protecting_person["health"] - res_dam_arm(atacked_person["damage"], protecting_person["armor"])), 2)
    if protecting_person["health"] <= 0:
        print(f"Игрок {protecting_person['name']} погибает, побеждает игрок {atacked_person['name']} с \033[31m{atacked_person['health']}\033[0m жизней")

while player1['health'] > 0 and player2['health'] > 0:
    attacked = input(f"Кто атакует? Игрок №1 - {player1_name}; или игрок №2 - {player2_name}. Введите номер игрока: ")
    attacked_view = input("Выберите вид боя: №1 - взаимные удары; №2 - односторонние удары. Введите номер вида: ")
    if attacked == '1':
        if attacked_view == '1':
            attack_vz(player1, player2)
        else:
            attack_odn(player1, player2)
    else:
        if attacked_view == '1':
            attack_vz(player2, player1)
        else:
            attack_odn(player2, player1)
