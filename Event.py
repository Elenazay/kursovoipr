#класс Мероприятие
from Category import *
MER = [] #Список мероприятий, как список проектов
mid = []
MR = ''

class Meropriatie:

    def __init__(self, id_m, cat_mer, name_m):
        self.id_m = id_m
        self.cat_mer = cat_mer
        self.name_m = name_m
        self.categories = []

    def add_cat(self):  # функция 4 для добавления категории через ввод
        id_c, name_c  = map(str, input("Введите ID и название категории (в ед.числе) через пробел: ").split())
        category = Category(id_c, name_c)
        self.categories.append(category)

    def add_all_cat(self): # функция 5 для добавления сразу всех категорий
        a = int(input('Введите количество категорий на мероприятии:'))
        for i in range(a):
            self.add_cat()

    def __str__(self):
        return (f'Мероприятие №{self.id_m} "{self.name_m}"')

# функция 10: объявление мероприятия
def Mer_vvod():
    a, cm, nm = map(str, input('Введите ID, категорию и название мероприятия, через запятую: ').split(','))
    d = nm[0]
    if d == ' ':
        nm = '' + nm[1:]
    d = cm[0]
    if d == ' ':
        nm = '' + nm[1:]
    mid.append(a)
    MR = Meropriatie(a, cm, nm)
    if MR in MER:
        a = int(a)
        if a == 0:
            a = a
        else:
            a = a - 1
        MR = MER[a]
        print("Удачной работы!")
    else:
        MER.append(MR)
        print("Вы добавили новое мероприятие")

# функция 6.1: записывает в файл список категорий на мероприятии
def Spisok_cat(MR, filename="spisok_category.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f'{MR.name_m}:\n')  # Запись названия мероприятия
            for category in MR.categories:
                file.write(str(category) + "\n")  # Запись информации о категории с новой строкой
    except Exception as fall:
        print(f"Ошибка при записи в файл: {fall}")

# функция 6.2: очищает список с категориями
def clear_Spisok_cat(filename="spisok_category.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            pass
    except Exception as e:
        print(f"Ошибка при очистке файла: {e}")

