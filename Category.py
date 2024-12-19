from Participant import *
# класс Категория
class Category:
    def __init__(self, id_c, name_c):
        self.id_c = id_c
        self.name_c = name_c
        self.people = []

    def add_uch(self, uchastnik):  # функция 2 для добавления участника напрямую через объекты
        self.people.append(uchastnik)

    def add_uch_vvod(self):  # функция 3 для добавления участника через ввод
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


# функция 7.1: записывает в файл список участников по категориям
def Spisok(ct, filename="spisok_text.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f'{ct.name_c}:\n')  # Запись названия категории
            for uchastnik in ct.people:
                file.write(str(uchastnik) + "\n")  # Запись информации об участнике с новой строкой
    except Exception as fall:
        print(f"Ошибка при записи в файл: {fall}")

# функция 7.2: очищает список участников
def clear_Spisok(filename="spisok_text.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            pass
    except Exception as e:
        print(f"Ошибка при очистке файла: {e}")

# функция 7.3 для обновления списка участников
def New_spisok(MR):
    k = 0
    clear_Spisok()
    for i in range(len(MR.categories)):
        Spisok(MR.categories[i])
        k += len(MR.categories[i].people)
    print(f'Количество зарегистрированных участников: {k} \n')