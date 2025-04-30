# Программа по генерации резюме

Программа предоставляет арі к
сгенерированному в формате html резюме

## Как установить

1. Клонируйте репозиторий: https://git.miem.hse.ru/ps-biv24x/vialchernenko.git
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте его:

- windows: `\venv|Scripts\activate'`
- unix: `source "/venv./bin/activate`

4. Создайте `.env` файл в формате:

```
token = <ваш токен на GitHub>
```

5. Загрузите зависимости: `pip install -r requirements.txt`

## Как запустить

1. 'python main.py'

## Как добавить новые зависимости

1. 'pip freeze > requirements.txt'
