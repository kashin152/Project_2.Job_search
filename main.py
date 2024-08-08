from config import VACANCIES_PATH_JSON
from src.saving_json import JSONSaver
from src.utils import user_choice_json


def main():
    """Запуск программы"""
    user_input = input(
        "Здравствуйте!\n"
        "Если вы желаете получить данные из файла нажмите 1\n"
        "Если вы желаете удалить данные из файла нажмите 2\n"
    )

    if user_input == "1":
        user_choice_json()
    elif user_input == "2":
        deleter = JSONSaver(VACANCIES_PATH_JSON)
        deleter.del_data()
        print("Данные удалены!")
    return


if __name__ == "__main__":
    main()
