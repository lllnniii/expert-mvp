# Diploma Project

Backend project based on FastAPI, PostgreSQL and Docker.

Technologies
Python 3.12
FastAPI
PostgreSQL
SQLAlchemy
Docker
Docker Compose
# Настройка проекта 

Клонирование репозитория
```bash
git clone git@github.com:lllnniii/expert-mvp.git
cd diploma
```
Открыть проект в редакторе, в корне проекта создать файл `.env` и добавить следующие переменные (порт должен быть свободный):
```
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres 
POSTGRES_DB=anyname 
POSTGRES_HOST=sevos 
POSTGRES_PORT=5432 

JWT_SECRET=secret 
JWT_EXPIRE_MINUTES=30 
REFRESH_EXPIRE_DAYS=7 

USE_SQLITE=False
```
Заупстите проект:
```bash 
docker compose up --build
```
API будет доступен в браузере по `http://127.0.0.1:8000`

Документация свагер `http://127.0.0.1:8000/api/docs` 
или редок если он больше нравится `http://127.0.0.1:8000/api/redoc`

Удалить контейнер:
```bash 
docker compose down -v
```
