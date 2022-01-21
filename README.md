## Разворачивание проекта
 <p>Когда проект будет загружен следует выполнить следующие команды: </p>

* Устанавливаем виртуальное окружение
```
sudo apt install python3-venv
```
* Активируем виртуальное окружение
```
python3 -m venv env
source env/bin/activate
```
* Устанавливаем библиотеки, которые требуются для запуска проекта
```
pip install -r requeriments.txt
```

* Есть возможность подключить базу postgreSQL для этого треубется открыть файл ```settings.py``` который находится в папке ``` freeflexProject ``` закомментировать данные по SQLite и разкоментировать для postgreSQL и ввести данные сервера

* Делаем миграцию базы данных
```
python manage.py makemigrations
python manage.py migrate
```
* Создаем суперпользователя
```
python manage.py createsuperuser
```
* Запускаем проект

``` 
python mnanage.py runserver
```

 
