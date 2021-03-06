# weather-bot

### Умный сервис прогноза погоды.

## Описание сервиса

Язык программирования `python`, библиотека `aiogram` для создания бота и `aiohttp` для запросов к внешнему сервису.

Реализована модель long polling бот - боту не требуется внешний IP и какой-либо деплой - можно запускать на любой машине, имеющей доступ к `api.telegram.org` (прокси можно использовать).

Формат ответа: текстовый шаблон вида `{локация}: {температура}, {погодный статус}`.

## Демо

[видео (YouTube)](https://www.youtube.com/watch?v=APs0A1dn28c)

## Процесс работы

- Пользователь отправляет боту название города или геолокацию.
- Из этих данных формируется запрос к [https://openweathermap.org/](openweathermap) и из полученного ответа получаются данные о температуре и погодном статусе (e.g. переменная облачность).
- Данные постобрабатываются для получения совета об одежде на основе правил на температуру и погодный статус.
- Результат отправляется пользователю текстовым сообщением.

## Как запустить

Желательно запускать в UNIX-like системе (Linux или Mac OS).

Добавить в переменные окружения ключ API Telegram (получается у [@BotFather](https://telegram.me/botfather) при создании нового бота командой /newbot) и ключ API [OpenWeatherMap](https://openweathermap.org/). И данные прокси-сервера для телеграм, если он не доступен. 

```
export TELEGRAM_API_TOKEN=...
export TELEGRAM_PROXY_URL=...
export TELEGRAM_PROXY_AUTH=...

export WEATHER_SERVICE_API_KEY=...
```

Для запуска необходим Python версии 3.7 и выше.

Установить зависимости:

```python
pip install -r requirements.txt
```

Запустить
```python
python3 weather_bot.py
```
