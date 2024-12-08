# service_desc

Технологии
* Python
* Django, Django REST Framework (DRF)
* PostgreSQL

## Как запустить проект:

### Клонировать репозиторий и перейти в него в командной строке:

`https://github.com/ivamari/service_desc.git`

`cd family_tree`

### Cоздать и активировать виртуальное окружение:

`python -m venv env`

`source venv/bin/activate`

### Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`

### Если БД не создана, создать ее в PostgreSQL, выполнив следующие команды:

Открыть PostgreSQL командой:
`psql -U your-database-user`

Создать БД:
`CREATE DATABASE your-database-name`

### Сгенерировать SECRET KEY командой:

`python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

### Скопировать файл .env.example в файл .env:

`cp .env.example .env`

### Заполнить переменные окружения в файле .env:
`SECRET_KEY=your-secret-key`

`DEBUG=True`

`ALLOWED_HOSTS=127.0.0.1 localhost`

``

`PG_DATABASE=your-database-name`

`PG_USER=your-database-user`

`PG_PASSWORD=your-database-password`

### Выполнить миграции:

`python manage.py migrate`

### Команда для загрузки фикстур статусов обращений:

`python manage.py loaddata ticket_status.json`

### Для создания суперпользователя:

`python manage.py createsuperuser`

### Запустить проект:

`python manage.py runserver`

Для перехода в админку: http://127.0.0.1:8000/admin/

Для перехода в документацию: http://127.0.0.1:8000/docs/

### Команда для запуска тестов:

`pytest`
