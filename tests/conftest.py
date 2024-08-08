import pytest

from config import VACANCIES_PATH_JSON
from src.job_filter import Vacancy
from src.saving_json import JSONSaver


@pytest.fixture
def vacancy():
    return Vacancy(
        "Менеджер по работе с клиентами",
        "https://hh.ru/vacancy/101709979",
        4_000_000,
        7_000_000,
        "Ташкент",
        "Опыт работы в продажах обязателен",
        "Консультирование клиентов",
    )


@pytest.fixture()
def vacancy2():
    return Vacancy(
        "Менеджер по работе с клиентами",
        "https://hh.ru/vacancy/101709979",
        40_000,
        70_000,
        "Ташкент",
        "Опыт работы в продажах обязателен",
        "Консультирование клиентов",
    )


@pytest.fixture()
def json_saver():
    return JSONSaver(filename=VACANCIES_PATH_JSON)
