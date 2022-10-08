from flask import Flask
import utils

#Создаем объект класса Flask
app = Flask(__name__)

#Прописываем роуты для объекта app
@app.route("/")
def page_all():
    """Роут для основного экрана 127.0.0.1:5000"""
    return f"<pre>{utils.get_all()}</pre>"


@app.route("/<int:pk>")
def page_candidate_pk(pk):
    """Роут для маршрута 127.0.0.1:5000/номер кандидата - поиск по номеру"""
    return f"<pre>{utils.get_by_pk(pk)}</pre>"


@app.route("/skills/<skill>")
def page_candidate_skill(skill):
    """Роут для маршрута 127.0.0.1:5000/skills/название навыка - поиск кандидата по навыку"""
    return f"<pre>{utils.get_by_skill(skill)}</pre>"

#Запуск app и сервера
app.run()
