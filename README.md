# Сервис скоринга

![Форма заявки](docs/form.png)

Сервис скоринга из [видео](https://youtu.be/XMG4RTdhzoI) на канале [мыш](https://www.youtube.com/channel/UCscWjyvPudzdIaGCCtEL3nw).

## Подготовка

Перед запуском сервиса скоринга и формы заявки нужно выполнить следующие шаги:

* Создайте папку `data` в корне проекта и скопируйте в нее файл `scoring.csv` из моей [Telegram группы](https://t.me/ml_mouse).
* (Опционально) Создайте виртуальное окружение для проекта с помощью `venv`, `poetry` или `uv`. Пример с использованием `venv`:

```shell
python3 -m venv .venv
source .venv/bin/activate
```

* Установите зависимости проекта:

```shell
pip3 install -r requirements.txt
```

* Обучите модель скоринга:

```shell
python3 train.py
```

Проверьте метрики модели и убедитесь, что в корне проекта появился файл `model.pkl`.

## Сервис скоринга

Запустите сервис скоринга с помощью команды:

```shell
uvicorn service:app
```

Запросы к сервису скоринга можно выполнить со страницы [Swagger UI](http://localhost:8000/docs), с помощью [Postman](https://www.postman.com/downloads), `curl` или другого HTTP клиента.

Также запросы можно выполнить из Python с помощью библиотеки `requests`:

```python
import requests

data = {"age": 27, "income": 50, "education": True, "work": True, "car": False}
response = requests.post("http://127.0.0.1:8000/score", json=data)
print(response.json())
```

## Форма заявки

Перед началом убедитесь, что запустили сервис скоринга. Откройте новое окно терминала и выполните команду:

```shell
streamlit run app.py
```

Страница с приложением при этом откроется автоматически. Если вы случайно закрыли ее, к ней можно вернуться по ссылке в логах либо по [этому адресу](http://localhost:8501).
