from Participant import *
from Category import *
from Event import *
from Badge import *
from Application import *

def one_launch():
    print("""
    Здравствуйте!
    Отличный день, чтобы собрать всех вместе и обсудить важные вопросы на мероприятии!
    """)
    Mer_vvod()

one_launch()

# добавление всех категорий на мероприятии
MER[0].add_all_cat()

# вывод списка категорий на мероприятии 1
Spisok_cat(MER[0])

# объявление участников
uch1 = Uchastnik(1, 'Зайцева', 'Елена', 'Сергеевна', '2006-5-26', 'ж', '89913002586','liberty_lena')
uch2 = Uchastnik(2, 'Белик', 'Мария', 'Владировна', '2003-6-22', 'ж', '88005553535', 'belik_mar')
uch3 = Uchastnik(3, 'Алексеева', 'Мария', 'Павловна', '2004-3-6', 'ж', '89870850036', 'ezsmary')
uch4 = Uchastnik(4, 'Черносвитова', 'Анна', 'Сергеевна', '2004-10-26', 'ж', '89875674523', 'anna_chern')

# добавление участников
MER[0].categories[0].add_uch(uch1)
MER[0].categories[1].add_uch(uch2)
MER[0].categories[1].add_uch(uch3)
MER[0].categories[0].add_uch(uch3)

# добавление участника с помощью ввода в категорию номер 1
MER[0].categories[0].add_uch_vvod()

# изменение статуса участника
uch1.change_status(2)
uch3.change_status(1)

# Обновление итогового списка
New_spisok(MER[0])

# Обновление файла с бейджами
New_badges(MER[0])

# Печать бейджа в ворд
Badge_w(MER[0])
