### Hexlet tests and linter status:
[![Actions Status](https://github.com/Krushovice/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Krushovice/python-project-52/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/f29d886940eb5e76a607/maintainability)](https://codeclimate.com/github/Krushovice/python-project-52/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/d41b9b1a511c0eb396b9/test_coverage)](https://codeclimate.com/github/Krushovice/python-project-52/test_coverage)




# Task manager
Менеджер задач для бизнеса, написанный на Django.
Поддерживает работу с пользователями, создание и делигирование задач, трекинг исполнения и т.д

### link: https://krushovice-task-manager.onrender.com


## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Тестирование](#тестирование)
- [Deploy и CI/CD](#deploy-и-ci/cd)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)


## Технологии
- [DJango](https://docs.djangoproject.com/en/5.0/)
- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [gunicorn](https://gunicorn.org/)


## Использование

Установите проект с помощью команды:
```sh
$ git clone https://github.com/Krushovice/python-project-52.git
```

И добавьте в свой проект файл .env c содержимым:
```
SECRET_KEY='Your secret key'
DEBUG=True
SQLITE_URL=sqlite:///my-local-sqlite.db
ACCESS_TOKEN='Your access token from server'

```

### Требования
Для установки и запуска проекта, необходим [Python](https://www.python.org/) v3.8.1 и больше


### Установка зависимостей
Для установки зависимостей, выполните команду:
```sh
$ make install
```

### Запуск Development сервера
Чтобы запустить сервер для разработки, выполните команду:
```sh
make start
```


## Тестирование

Данный проект покрыт django-tests. Для их запуска выполните команду:
```sh
make test
```

## Deploy и CI/CD
Для того, чтобы задеплоить данный проект на бесплатный хостинг [Render](https://render.com/), можно воспользоваться вот этим гайдом: [Гайд](https://docs.render.com/deploy-django)


### Зачем вы разработали этот проект?
Это дипломный проект в рамках обучения по направлению Python-разработчик на платформе [Hexlet](https://ru.hexlet.io/)


## Команда проекта
- [Башкатов Алексей](kickstar69@yandex.ru ) — Python-developer

Если у вас есть вопросы или замечния по данному проекту можете написать мне на почту
