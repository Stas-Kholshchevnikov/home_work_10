import json
import os

def load_candidates():
    """Открытие файла и сохранение значения в переменную"""
    with open(os.path.join('candidates.json'), 'r', encoding='UTF-8') as file:
        return json.load(file)

def get_all():
    """Функция вывода полного списка кандидатов"""
    result = ''
    candidate_list = load_candidates()
    for i in range(len(candidate_list)):
        result += (f"Имя кандидата - {candidate_list[i]['name']}\n"
                   f"Позиция кандидата - {candidate_list[i]['position']}\n"
                   f"Навыки - {candidate_list[i]['skills']}\n\n\n")
    return result

def get_by_pk(pk):
    """Функция поиска кандидата по номеру"""
    result = ''
    candidate_list = load_candidates()
    for item in candidate_list:
        if item["pk"] == pk:
            result += (f"<img src='({item['picture']})'>\n\n"
                       f""f"Имя кандидата - {item['name']}\n"
                       f"Позиция кандидата - {item['position']}\n"
                       f"Навыки - {item['skills']}\n\n\n")
    return result

def get_by_skill(skill_name):
    """Функция поиска кандидата по навыку"""
    result = ''
    candidate_list = load_candidates()
    for item in candidate_list:
        if skill_name.lower() in item["skills"].replace(" ", "").lower().split(","):
            result += (f"Имя кандидата - {item['name']}\n"
                       f"Позиция кандидата - {item['position']}\n"
                       f"Навыки - {item['skills']}\n\n\n")
    return result