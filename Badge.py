from docxtpl import DocxTemplate

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

# функция 8.1: для генерации всех бейджей в файл
def Generate_badges(meropriatie, category):
    with open('badges.txt', 'a', encoding='utf-8') as file:  # открываем файл для записи
        for people in category.people:
            badge = Badge(people, meropriatie, category)
            file.write(str(badge) + '\n')  # записываем бейдж в файл

# функция 8.2: очищает файл с бейджами
def clear_Badges(filename="badges.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            pass
    except Exception as e:
        print(f"Ошибка при очистке файла: {e}")

# функция 8.3 для обновления файла с бейджами
def New_badges(MR):
    clear_Badges()
    for i in range(len(MR.categories)):
        Generate_badges(MR, MR.categories[i])

# функция 9: выводит бейдж участника в Word
def Badge_w(MR):
    try:
        doc = DocxTemplate("бейдж.docx")
        c = int(input('Генерация бейджа. Введите ID категории: ')) - 1
        u = int(input('Генерация бейджа. Введите ID участника: ')) - 1
        context = {'name_m': MR.name_m, 'cat_mer': MR.cat_mer,
                   'familia': MR.categories[c].people[u].familia, 'ima': MR.categories[c].people[u].ima,
                   'teleg': MR.categories[c].people[u].teleg, 'name_c': MR.categories[c].name_c}
        doc.render(context)
        doc.save("бейдж-final.docx")
    except IndexError:
        print('Нет такого участника в категории, попробуйте изменить ID категории или участника')