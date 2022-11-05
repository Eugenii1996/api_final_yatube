# Проект API социальной сети Yatube

### О проекте:

Приложение представляет собой интерфейс для обмена данными социальной сети Yatube.
Предоставляет клиентам доступ к базе данных.
Данные передаются в формате JSON.
В реализации проекта применена архитектура REST API.

### Как запустить проект на Windows:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Eugenii1996/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3.7 -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов к API:

POST-запрос на эндпоинт api/v1/posts/:

```
{
    "text": "string",
    "image": "string",
    "group": 1
}
```

Ответ:

```
{
    "id": 1,
    "author": "username",
    "text": "string",
    "pub_date": "2022-03-13T14:15:22Z",
    "image": "string",
    "group": 1
}
```

GET-запрос на эндпоинт api/v1/posts/{post_id}/comments/ вернет список комментариев к посту:

```
[
    {
        "id": 1,
        "author": "username",
        "text": "string",
        "created": "2022-03-13T14:15:22Z",
        "post": 1
    },
    {
        "id": 2,
        "author": "username",
        "text": "string",
        "created": "2022-03-13T14:15:22Z",
        "post": 1
    }
]
```
