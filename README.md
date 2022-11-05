# Проект API социальной сети Yatube

### Разработчик:

 - [Мирошниченко Евгений Игоревич](https://github.com/Eugenii1996)

### О проекте:

Проект Yatube представляет собой социальную сеть, в которой пользователи имеют возможность создать учетную запись, 
публиковать записи, подписываться на любимых авторов и отмечать понравившиеся записи.
В данном проекте реализован интерфейс для обмена данными социальной сети Yatube.
Он предоставляет клиентам доступ к базе данных. Данные передаются в формате JSON.

Примененные технологии:
 - Python 3
 - Django Rest Framework
 - Git
 - Pytest

### Клонирование репозитория и переход в него в командной строке:

```bash
git clone git@github.com:Eugenii1996/api_final_yatube.git
```

```bash
cd api_final_yatube
```

### Cоздать и активировать виртуальное окружение:

Виртуальное окружение должно использовать Python 3.7

```bash
pyhton -m venv venv
```

* Если у вас Linux/MacOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

### Установка зависимостей из файла requirements.txt:

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

### Выполнить миграции:

```bash
python manage.py migrate
```

### Запуск проекта:

```bash
python manage.py runserver
```

### Примеры запросов к API:

POST-запрос на эндпоинт api/v1/posts/:

```bash
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

Документация к API находится по пути: api_final_yatube/yatube_api/static/redoc.yaml
