# README #

Основной репозиторий
https://threat0day@bitbucket.org/threat0day/library_sppr.git

приложение https://libraryspprbackend.herokuapp.com/

### Проблемы ###

* Разобраться с сабмодулями гита и работать с одним репозиторием для хероку и битбакета
* нужно вручную делать минификацию приложений на react (npm run "watch")
* у бесплатного тарифа ограничение 10к строк

### Заметки ###

* миграции на хероку
  heroku run python manage.py migrate
  
### Другие документы ###

https://docs.google.com/document/d/1JJW-KA1AwRF3RJui7isBWd94yUBP4d-NlKt9gqweC20/edit?usp=sharing

### Задачи ###

* Связать таблицы
* Поменять описание таблиц и форматы
* CRUD АПИ
* конвертнуть датасет из файлов


### Не срочные Задачи ###
* Тесты


### Доступ к БД ###
Host
ec2-44-199-86-61.compute-1.amazonaws.com
Database
d5qmfpg157vqnq
User
chxriemofmzckk
Port
5432
Password
03ee7070a8c5b5ee9a383ac20eaf595d817d594e5813e872b0fc24cb62063804
URI
postgres://chxriemofmzckk:03ee7070a8c5b5ee9a383ac20eaf595d817d594e5813e872b0fc24cb62063804@ec2-44-199-86-61.compute-1.amazonaws.com:5432/d5qmfpg157vqnq
Heroku CLI
heroku pg:psql postgresql-clear-76785 --app libraryspprbackend