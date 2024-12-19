from Participant import Uchastnik
class Zaiavka:
    def __init__(self, id_z, deiat, dostizh, naviki, ssilka, uchastnik, badge=None):
        self.id_z = id_z
        self.deiat = deiat
        self.dostizh = dostizh
        self.naviki = naviki
        self.ssilka = ssilka
        self.uchastnik = uchastnik
        self.badge = badge #  Ссылка на объект Badge (может быть None)

    def __str__(self):
        result = f"""
                    ----- Заявка № {self.id_z} -----

                    --- {self.uchastnik.familia} {self.uchastnik.ima} ---
                    Деятельность: {self.deiat}

                    Достижения: {self.dostizh}

                    Навыки:{self.naviki}

                    Ссылка на видеовизитку(при наличии): {self.ssilka}

                    Telegram: @{self.uchastnik.teleg}

                    """
        if self.badge:
            result += "\n---Информация о бейдже---\n" + str(self.badge)
        return result
