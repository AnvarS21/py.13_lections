# 1. Создать виртуальное окружение
#         python3 -m venv venv
# 2. Устанавливаем нужные библиотеки и джанго
#         pip install <library>
#         pip freeze > requirements.txt
# 3. Создание проекта и файла manage.python3
#         django-admin startproject <name>
# 4. Создание приложения для проекта
#         python3 manage.py startapp <name>
#         django-admin startapp <name>





# 5. Записать название вашего приложения в installed apps в настройках (подключение вашего приложения в проект)

# 6. Настройка базы данных

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'firstapi_db',
#         'USER': 'anvar',
#         'PASSWORD': '1',
#         'HOST': 'localhost',
#         'PORT': 5432
#     }
# }

# 7. Создание базы данных в постгресс
# 8. Работа с миграциями
#     8.1 Создаем файлы миграциями
#         python3 manage.py makemigratioins
#     8.2 Запускаем файлы миграциями
#         python3 manage.py migrate

# Запуск сервера
#     python3 manage.py runserver

# Создание суперюзера
#     python3 manage.py createsuperuser