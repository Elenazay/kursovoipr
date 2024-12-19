from docxtpl import DocxTemplate

MER = []
# класс Участник
class Uchastnik:
    def __init__(self, id_uch, familia, ima, otchestvo, data_rozh, pol, phone, teleg, status="registered"):
        self.id_uch = id_uch
        self.familia = familia
        self.ima = ima
        self.otchestvo = otchestvo
        self.data_rozh = data_rozh
        self.pol = pol
        self.phone = phone
        self.teleg = teleg
        self.status = status
        self.allowed_statuses = {0:"registered", 1:"prisutstvoval", 2:"otsutstvoval"}

    def __str__(self):
        return (f'{self.familia} {self.ima} {self.otchestvo} {self.data_rozh} {self.pol} {self.phone} {self.teleg} {self.status}')

    def change_status(self, new_status): #функция изменения статуса
        self.status = self.allowed_statuses[new_status]

# класс Категория
class Category:
    def __init__(self, id_c, name_c):
        self.id_c = id_c
        self.name_c = name_c
        self.people = []

    def add_uch(self, uchastnik):  # функция добавления участника напрямую через объекты
        self.people.append(uchastnik)

    def add_uch_vvod(self):  # функция добавления участника через ввод
        id_uch = int(input("Введите ID нового участника: "))
        familia = input("Фамилия: ")
        ima = input("Имя: ")
        otchestvo = input("Отчество: ")
        data_rozh = input("Дата рождения (в формате гггг-мм-дд): ")
        pol = input("Пол (м/ж): ")
        phone = input("Телефон (в формате 8XXXXXXXXXX): ")
        teleg = input("Username в телеграмм: ")
        uchastnik = Uchastnik(id_uch, familia, ima, otchestvo, data_rozh, pol, phone, teleg, status='registered')
        self.people.append(uchastnik)

    def __str__(self):
        return (f'{self.id_c} {self.name_c}')


#класс Мероприятие
class Meropriatie:

    def __init__(self, id_m, cat_mer, name_m):
        self.id_m = id_m
        self.cat_mer = cat_mer
        self.name_m = name_m
        self.categories = []

    def add_cat(self):  # функция добавления категории через ввод
        id_c, name_c  = map(str, input("Введите ID и название категории (в ед.числе) через пробел: ").split())
        category = Category(id_c, name_c)
        self.categories.append(category)

    def add_all_cat(self): # функция добавления сразу всех категорий
        a = int(input('Введите количество категорий на мероприятии:'))
        for i in range(a):
            self.add_cat()

    def __str__(self):
        return (f'Мероприятие №{self.id_m} "{self.name_m}"')


# функция 1: записывает в файл список категорий на мероприятии
def Spisok_cat(MR, filename="spisok_category.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f'{MR.name_m}:\n')  # Запись названия мероприятия
            for category in MR.categories:
                file.write(str(category) + "\n")  # Запись информации о категории с новой строкой
    except Exception as fall:
        print(f"Ошибка при записи в файл: {fall}")

# функция очищает список с категориями
def clear_Spisok_cat(filename="spisok_category.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            pass
    except Exception as e:
        print(f"Ошибка при очистке файла: {e}")

# функция 2: записывает в файл список участников по категории
def Spisok(ct, filename="spisok_text.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f'{ct.name_c}:\n')  # Запись названия категории
            for uchastnik in ct.people:
                file.write(str(uchastnik) + "\n")  # Запись информации об участнике с новой строкой
    except Exception as fall:
        print(f"Ошибка при записи в файл: {fall}")

# очищает список участников
def clear_Spisok(filename="spisok_text.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            pass
    except Exception as e:
        print(f"Ошибка при очистке файла: {e}")

# класс Бейдж для создания бейджа
class Badge:
    def __init__(self, uchastnik, meropriatie, category):
        self.uchastnik = uchastnik
        self.meropriatie = meropriatie
        self.category = category

    def __str__(self):
        return f"""
        ----- {self.meropriatie.name_m} -----

        --- {self.uchastnik.familia} {self.uchastnik.ima} ---
        ------ {self.category.name_c} ------
        Telegram: @{self.uchastnik.teleg}

        """

# функция для генерации бейджей
def Generate_badges(meropriatie, category):
    with open('badges.txt', 'a', encoding='utf-8') as file:  # открываем файл для записи
        for people in category.people:
            badge = Badge(people, meropriatie, category)
            file.write(str(badge) + '\n')  # записываем бейдж в файл

# очищает файл с бейджами
def clear_Badges(filename="badges.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            pass
    except Exception as e:
        print(f"Ошибка при очистке файла: {e}")

# функция для обновления списка участников
def New_spisok(MR):
    k = 0
    clear_Spisok()
    for i in range(len(MR.categories)):
        Spisok(MR.categories[i])
        k += len(MR.categories[i].people)
    print(f'Количество зарегистрированных участников: {k} \n')


# функция для обновления бейджей
def New_badges(MR):
    clear_Badges()
    for i in range(len(MR.categories)):
        Generate_badges(MR, MR.categories[i])

# функция выводит бейдж участника в Word
def Badge_w(MR):
    doc = DocxTemplate("бейдж.docx")
    c = int(input('Генерация бейджа. Введите ID категории: ')) - 1
    u = int(input('Генерация бейджа. Введите ID участника: ')) - 1
    context = {'name_m': MR.name_m, 'cat_mer': MR.cat_mer,
            'familia': MR.categories[c].people[u].familia, 'ima': MR.categories[c].people[u].ima , 'teleg': MR.categories[c].people[u].teleg, 'name_c':MR.categories[c].name_c}
    doc.render(context)
    doc.save("бейдж-final.docx")

# объявление мероприятия 1
def Mer_vvod():
    a, cm, nm = map(str, input('Введите ID, категорию и название мероприятия, через запятую: ').split(','))
    d = nm[0]
    if d == ' ':
        nm = '' + nm[1:]
    MR = Meropriatie(a, cm, nm)
    MER.append(MR)
