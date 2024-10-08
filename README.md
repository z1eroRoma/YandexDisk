# YandexDisk

**Описание веб-приложения**

Данное веб-приложение разработано на Django и предназначено для взаимодействия с API Яндекс.Диска. Приложение предоставляет возможность просмотра файлов, размещённых по публичной ссылке на Яндекс.Диске, и их последующего скачивания. Оно имеет следующий функционал:

1. **Просмотр файлов по публичной ссылке**:
   - Пользователь может ввести публичную ссылку на содержимое Яндекс.Диска.
   - После обработки ссылки приложение отображает список доступных файлов и папок.
2. **Загрузка файлов**:
   - Пользователь может выбрать отдельные файлы из списка и скачать их на свой локальный компьютер.
   - Каждый файл представлен в виде карточки с иконкой, названием файла и кнопкой "Скачать".
3. **Фильтрация файлов**:
   - Существует возможность фильтрации файлов по типу (например, только изображения, документы и т.д.).
4. **Кэширование**:
   - Список файлов кэшируется, чтобы не перегружать API Яндекс.Диска многократными запросами.
5. **Адаптивный интерфейс**:
   - Веб-интерфейс выполнен с использованием Bootstrap и имеет современный дизайн.
   - На странице с файлами карточки отображаются по три в ряд на больших экранах и адаптируются под мобильные устройства.
6. **Множественное скачивание** (опционально):
   - Пользователь может выбрать несколько файлов и скачать их одновременно.
   
### Особенности приложения:
- Простота использования: интуитивно понятный интерфейс для работы с файлами.
- Безопасность: взаимодействие с API Яндекс.Диска происходит через публичные ссылки, а сам процесс аутентификации с Яндекс.Диском не требуется.

---

### Инструкция по запуску приложения

#### Требования:
1. **Python 3.8+**
2. **Django 4.x**
3. **Библиотека `requests` для работы с API Яндекс.Диска**
4. **Менеджер пакетов pip для установки зависимостей**

#### Шаги по установке и запуску:

##### 1. Клонирование репозитория
Сначала необходимо клонировать репозиторий с кодом проекта. Введите следующую команду в терминале:

```bash
git clone <URL_репозитория>
```

##### 2. Переход в директорию проекта
Перейдите в директорию проекта:

```bash
cd <название_директории>
```

##### 3. Создание виртуального окружения
Создайте виртуальное окружение для изоляции зависимостей проекта:

```bash
python -m venv venv
```

Активируйте виртуальное окружение:
- На Windows:
    ```bash
    venv\Scripts\activate
    ```
- На MacOS/Linux:
    ```bash
    source venv/bin/activate
    ```

##### 4. Установка зависимостей
Установите все необходимые зависимости, которые указаны в файле `requirements.txt`. Выполните команду:

```bash
pip install -r requirements.txt
```

##### 5. Миграции базы данных
Приложению необходимо настроить базу данных Django. Выполните миграции:

```bash
python manage.py migrate
```

##### 6. Запуск сервера разработки
Теперь можно запустить сервер разработки Django:

```bash
python manage.py runserver
```

##### 7. Доступ к приложению
После запуска сервера вы сможете получить доступ к приложению по адресу:

```
http://127.0.0.1:8000/
```

##### 8. Ввод публичной ссылки на Яндекс.Диск
- На главной странице приложения введите публичную ссылку на файлы, размещённые на Яндекс.Диске.
- После этого вы попадёте на страницу со списком файлов, где сможете их просмотреть, отфильтровать по типу и скачать.

##### 9. Остановка сервера
Чтобы остановить сервер, просто нажмите `CTRL+C` в терминале.

---

### Полезные команды для разработки
- **Создание нового суперпользователя (если требуется доступ к админке)**:
  ```bash
  python manage.py createsuperuser
  ```
- **Обновление миграций (при изменении моделей базы данных)**:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- **Запуск Django shell (для выполнения команд в интерактивной среде Django)**:
  ```bash
  python manage.py shell
  ```

---
