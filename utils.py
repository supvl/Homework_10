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
    display = '<pre>\t\tВсе кандидаты:\n'
    for candidate in data_candidates:
        display += f""" 
                   Имя - {candidate['name']}
                   Позиция - {candidate['position']}
                   Навыки - {candidate['skills']}
                   """
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


def get_by_skill(skill_name: str) -> str:
    data_candidates = load_candidates()
    display = f'<pre>\t\tKандидаты с навыком {skill_name}:\n'
    for candidate in data_candidates:
        if skill_name.lower() in candidate['skills'].lower().split(", "):
            display += f"""            
                       Имя - {candidate['name']}
                       Позиция - {candidate['position']}
                       Навыки - {candidate['skills']}
                       """
    display += '</pre>'
    return display

