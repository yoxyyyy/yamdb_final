# yamdb_final

![example workflow](https://github.com/yoxyyyy/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)


Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории:«Книги», «Фильмы», «Музыка». Список категорий  может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Настроика для приложения Continuous Integration и Continuous Deployment, реализация:
- автоматический запуск тестов,
- обновление образов на Docker Hub,
- автоматический деплой на боевой сервер при пуше в главную ветку main.

Стек:
- Django 4.1.1
- DRF 3.14.0
- djangorestframework-simplejwt 5.2.1
- psycopg2-binary 2.9.3
- PyJWT 2.5.0
