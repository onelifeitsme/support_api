# supp

Установнка:
1. docker-compose build
2. docker-compose up
3. В другом окне терминала docker ps, скопировать id контейнера на образе supp_supp и выполнить:
docker exec -it {id} python manage.py createsuperuser

URLS:
1. Регистрация пользователя: http://127.0.0.1:8000/api-auth/users/
Создаётся методом post.
2. Получение токена: http://127.0.0.1:8000/api-auth/jwt/create
Создаётся методом post.
3. Просмотр тикетов: http://127.0.0.1:8000/api/v1/tickets/
get-запрос выводит все существующие тикеты (с пагинацией 20), если тикеты запрашивает юзер-сотрудник. Если запрашивает клиент без статуса персонала, то отдаются только его тикеты.
Доступные для персонала параметры в get-запросе: "status": "В очереди", "status": "Принят в работу", "status": "Отвечен", "status": "Вопрос решён".
post-запрос создаёт новый тикет.
4. Просмотр конкретного тикета: http://127.0.0.1:8000/api/v1/ticket/<int:pk>
path-запрос изменяет текущий тикет. В случае изменения статуса, на почту создателя тикета приходит письмо.
5. Просмотр сообщений в тикете: http://127.0.0.1:8000/api/v1/ticket/<int:pk>messages
get-запрос выводит сообщения тикета. post-запрос создаёт новое сообщение.
6. Визуальное отображение API: http://127.0.0.1:8000/docs/
