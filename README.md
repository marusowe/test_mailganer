### Тестовое задание Mailganer
Написать на Python 2.7 / Django небольшой сервис отправки имейл рассылок.
Возможности сервиса:
 1. Отправка рассылок с использованием html макета и списка подписчиков.
 2. Отправка отложенных рассылок.
 3. Использование переменных в макете рассылки. (Пример: имя, фамилия, день рождения из списка подписчиков)
 4. Отслеживание открытий писем.  

Отложенные отправки реализовать при помощи Celer

### Запуск
1. Создать файл с переменным окружения согласно шаблону `.env.sample` в корне проекта
2. Собрать контейнер `docker-compose build`
2. Запустить контейнер `docker-compose up`