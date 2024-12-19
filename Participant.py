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

    def change_status(self, new_status): #функция 1 для изменения статуса участника
        try:
            self.status = self.allowed_statuses[new_status]
        except ValueError as e:
            print(f"Ошибка изменения статуса: {e}")

