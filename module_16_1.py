from fastapi import FastAPI
# импорт класс FastAPI

app = FastAPI()
#приложение(объект) FastAPI

@app.get("/")
async def main_page() -> dict:
    #Создание маршрута к главной странице - "/".
    # По нему должно выводиться сообщение "Главная страница".
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin_page() -> dict:
    #Создание маршрута к странице админа - "user/admin".
    # По нему должно выводиться сообщение "Вы вошли как администратор".
    return {"message": "Вы вошли как администратор"}


@app.get('/user/{user_id}')
async def get_user_id(user_id: int) -> dict:
    # Создание маршрута к страницам пользователей - '/user/{user_id}'.
    # По нему должно выводиться сообщение "Вы вошли как администратор".
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def get_user_info(username: str, age: int) -> dict:
    #маршрут к страницам пользователей передавая данные  в адресной строке - "/user"
    return {'message':
            f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

#uvicorn module_16_1:app --reload запуск сервера
#http://127.0.0.1:8000
#netstat -aon | findstr :8000
#taskkill /PID 4148 /F

#http://127.0.0.1:8000 - Создайте маршрут к главной странице
#http://127.0.0.1:8000/user/admin - Создайте маршрут к странице администратора
#http://127.0.0.1:8000/user/23 - Создайте маршрут к страницам пользователя 23
#http://127.0.0.1:8000/user?username='Vlad'&age=57 Создайте маршрут к страницам
# пользователей передавая данные в адресной строке