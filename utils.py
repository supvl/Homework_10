import json


def load_candidates() -> list[dict]:
    """
    Получение данных из JSON-файла
    :param file_json: JSON-файл откуда берутся данные
    :return: список с данными, полученными из JSON-файла
    """
    file_json = "candidates.json"
    with open(file_json, mode='r', encoding='utf-8') as file:
        data_candidates = json.load(file)
    return data_candidates


def get_all() -> str:
    data_candidates = load_candidates()
    display = '<pre>Все кандидаты:\n\n'
    for candidate in data_candidates:
        display += f"\tИмя - {candidate['name']}\n" \
                   f"\tПозиция - {candidate['position']}\n" \
                   f"\tНавыки - {candidate['skills']}\n\n"
    display += '</pre>'
    return display


def get_by_pk(pk: int) -> str:
    data_candidates = load_candidates()
    for candidate in data_candidates:
        if candidate['pk'] == pk:
            display = f"""
                    <img src = "{candidate['picture']}">\n
                    <pre>\n
                    \tИмя - {candidate['name']}\n
                    \tПозиция - {candidate['position']}\n
                    \tНавыки - {candidate['skills']}\n
                    </pre>
                    """
            return display
        else:
            return 'Нет такого кандидата'
