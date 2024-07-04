# sport_channel

sport_channel - веб приложение с каталогом новостей и магазином спорттоваров. Реализована система регистрации и авторизации пользователей, система комментариев, публикация товаров.

# Руководство по запуску

+ Клонируйте репозиторий
+ Создайте виртуальное окружение и активируйте его:

#### Windows
```
python -m venv .venv
.venv\Scripts\activate
```

#### Linux
```
python3 -m venv .venv
source .venv/bin/activate
```

+ Установите зависимости:

```
pip install -r requirements.txt
```

+ На вашей операционой системе должен быть установлен PostgreSQL
+ Создайте базу данных sport_db в PotgreSQL
+ Проведите миграции командой:

#### Windows
```
python manage.py migrate
```

#### Linux
```
python3 manage.py migrate
```

+ Создайте суперпользователя для  входа в админ панель:

#### Windows
```
python manage.py createsuperuser
```

#### Linux
```
python3 manage.py createsuperuser
```

+ Запустите приложение:

#### Windows
```
python manage.py runserver
```

#### Linux
```
python3 manage.py runserver
```

+ Откройте браузер и перейдите по адресу http://127.0.0.1:8000/main/. Поздравляю, теперь вы можете пользоваться моим приложением :wink:


# Для тех, кому лень запускать приложение, чтобы насладиться визуалом:

Главная    |  Профиль
:-------------------------:|:-------------------------:
![](https://github.com/GGGamzat/sport_channel/blob/main/images/1.png)  |  ![](https://github.com/GGGamzat/sport_channel/blob/main/images/4.png)  


Регистрация   |  Авторизация
:-------------------------:|:-------------------------:
![](https://github.com/GGGamzat/sport_channel/blob/main/images/2.png)  |  ![](https://github.com/GGGamzat/sport_channel/blob/main/images/3.png)


Товары    |  Подробнее товар
:-------------------------:|:-------------------------:
![](https://github.com/GGGamzat/sport_channel/blob/main/images/6.png) |  ![](https://github.com/GGGamzat/sport_channel/blob/main/images/7.png)

Новости   |  Подробнее новость
:-------------------------:|:-------------------------:
![](https://github.com/GGGamzat/sport_channel/blob/main/images/5.png) |  ![](https://github.com/GGGamzat/sport_channel/blob/main/images/9.png)

# Автор

Абдуллаев Гамзат