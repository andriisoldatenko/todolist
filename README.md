How to setup
========

pip install -r requirements.txt

manage.py syncdb

Simple Rest Api
===

Create
curl -i --user test:test -H "Content-Type: application/json" -H "Accept: application/json" -X POST \
--data '{"done": false, "priority": 2, "title": "asdasd task", "user": "/api/v1/auth/user/2/"}' http://127.0.0.1:8000/api/v1/task/

Update
curl -i --user test:test -H "Content-Type: application/json" -H "Accept: application/json" -X PATCH \
--data '{"second": "second task"}' http://127.0.0.1:8000/api/v1/task/5/

Delete
curl -i --user test:test --dump-header - -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/api/v1/task/5/