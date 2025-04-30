from jinja2 import Template
from datetime import datetime
from dotenv import load_dotenv
import os
import requests  # Добавляем импорт для работы с API

TEMPLATE_FILE_NAME = "./templates/index.html"
INDEX_FILE_NAME = "./public/index.html"

# Загружаем переменные окружения из .env
load_dotenv()
token = os.getenv("token")


def data_Git(token):
    """Получение данных пользователя и репозиториев с GitHub API"""
    user_url = "https://api.github.com/user"
    repos_url = "https://api.github.com/user/repos"

    headers = {
        'Authorization': f'token {token}',
        'Accept': "application/json"
    }

    user_response = requests.get(user_url, headers=headers)
    if user_response.status_code != 200:
        raise Exception(
            f"Ошибка при запросе данных пользователя: {user_response.status_code}")

    user_data = user_response.json()

    repos_response = requests.get(repos_url, headers=headers)
    if repos_response.status_code != 200:
        raise Exception(
            f"Ошибка при запросе репозиториев: {repos_response.status_code}")

    repos_data = repos_response.json()

    info_about_user = {
        "name": user_data.get("name", "Не указано"),
        "login": user_data.get("login", ""),
        # Email может быть скрыт, если не публичный
        "email": user_data.get("email", "Не указано"),
        "bio": user_data.get("bio", "Нет описания"),
        "location": user_data.get("location", "Не указано"),
        "repos_url": user_data.get("repos_url", "")
    }
    all_repositories = [
        {
            "name": repo["name"],
            "url": repo["html_url"]
        } for repo in repos_data
    ]
    return info_about_user, all_repositories


def generate_api():
    """Генерация HTML-файла с данными из GitHub"""
    # Получаем данные из GitHub
    info_about_user, all_repositories = data_Git(token)

    with open(TEMPLATE_FILE_NAME, "r", encoding="utf-8") as template_file:
        template_text = template_file.read()
        jinja_template = Template(template_text)
        rendered_api = jinja_template.render(
            info_about_user=info_about_user,
            all_repositories=all_repositories,
            datetime=datetime.now()
        )
        with open(INDEX_FILE_NAME, "w", encoding="utf-8") as api_file:
            api_file.write(rendered_api)


def get_api():
    """Чтение сгенерированного HTML-файла"""
    with open(INDEX_FILE_NAME, "r", encoding="utf-8") as f:
        return f.read()
