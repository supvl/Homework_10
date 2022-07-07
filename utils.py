import json


def load_candidates() -> list[dict]:
    """
    Получение данных из JSON-файла
    :return: список словарей с данными, полученными из JSON-файла
    """
    file_json = "candidates.json"
    with open(file_json, mode='r', encoding='utf-8') as file:
        data_candidates = json.load(file)
    return data_candidates


def get_all() -> str:
    data_candidates = load_candidates()
    display = '<pre>\tВсе кандидаты:\n\n'
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
                    <pre>
                    \tКандидат номер {pk}:\n
                    <img src = "{candidate['picture']}">
                    <pre>
                    Имя - {candidate['name']}
                    Позиция - {candidate['position']}
                    Навыки - {candidate['skills']}
                    </pre>
                    """
            return display
    return "\tНет кандидата с таким номером"
