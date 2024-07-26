from abc import ABC, abstractmethod

import requests


class GetApiHH(ABC):

    """Абстрактный класс для подключения к API"""

    @abstractmethod
    def load_vacancies(self):
        pass


class ApiHH(GetApiHH):

    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {"text": "", "page": 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, params=self.params)
            vacancies = response.json()['items']
            return vacancies


if __name__ == "__main__":
    list_vacancies = ApiHH()
    vacancies = list_vacancies.load_vacancies("Тестировщик")
    print(vacancies)
