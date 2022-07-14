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

bash install.sh
Далее выбор между обычной установкой и с испольсзованием docker
```
## Запуск при обычной установке:
```
python3 manage.py runserver
```  
## Запуск при установке через docker:
```
docker-compose up -d
```  
### Для более приятного внешнего вида сайта:  
```python3 manage.py runserver --insecure```