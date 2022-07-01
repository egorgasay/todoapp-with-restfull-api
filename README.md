# TODO app with RESTfull API
![Логотип](https://user-images.githubusercontent.com/102957432/176931773-9af8950b-e4c5-47b0-89b1-9e638d4a6524.png)

## API
```/tasks/all - список всех задач```  
```/tasks/<id> - получение конкретной задачи по id```  
```/create/ - создание новой задачи```  
```/change-status/<id> - изменить статус задачи```  
```/delete/<id> - удалить задачу```  

  
## Запуск тестов:
```
pytest tests/*  
```
## Установка:
```
git clone https://github.com/egorgasay/todoapp-with-restfull-api

cd todoapp-with-restfull-api

python3 -m pip install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver
```