Проект выполняет следующие функции:
1) Получение данных с документа при помощи Google API (googleSheetSite/sheet/ExternalAPI/GoogleAPI.py)
2) Добавление данных в БД на основе PostgreSQL (реализовано при помощи django orm)
3) Перевод данных в рубли при помощи API ЦБ РФ (googleSheetSite/sheet/ExternalAPI/CBR_API.py)
4) Постоянная работа скрипта обеспечена при помощи Celery
5) Ежедневная (в 9:00) проверка данных из бд на предмет пропуска срока поставки и сообщает через телеграм-бот о том, срок поставки
каких заказов был пропущен
6) Обеспечение работы одностраничного web-приложения на основе django, которое предоставляет доступ к данным из бд и обновляет их
в режиме рельного времени на основе react.js

Инструкция:
Проект упакован в docker контейнер и для его запуска следует клонировать проект с github и запустить команду "docker-compose up"
После этого приложение должно самостоятельно развернуться в полном объеме и начать работу.
Одностраничное приложение должно быть доступно по адресу http://0.0.0.0:8000/ или http://127.0.0.1:8000/
Телеграм бот для подписки на рассылку: @google_sheet_interview_bot

Изменить интервал сообщений для бота можно в файле googleSheetSite/sheet/tasks.py в функции setup_periodic_tasks

Проектом предусмотрен более изящный способ полуения информации с google Sheets, но для его реализации необходимо, чтобы был известен 
URL приложения (К таблице написан простой скрипт, который способен при внесении изменений направлять сиграл по введенному адресу).
Таким образом можно избежать постоянного обращения к Google API. Подробности в файле googleSheetSite/sheet/views.py