# Базовый образ с Python 3.9, минимальная версия
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt для кэширования зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    pip show flask

# Копируем все файлы в рабочую директорию
COPY . /app/

# Задаем точку входа для запуска приложения
ENTRYPOINT ["python3", "/app/main.py"]