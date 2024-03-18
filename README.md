# Python-скрипт по получению погоды в заданном городе

## Используемые библиотеки

- ***requests*** для работы с get-запросом на внешний API
- ***json*** для представления результата get-запроса в Json формате
- ***datetime*** для формирования строки-времени в часовом поясе пользователя

## Используемый API

***<http://api.openweathermap.org>*** - API для работы с погодой
Для работы используется api_key, который пользователь должен получить в зарегистрированном аккаунте.
На данный момент стоит ключ разработчика

## Запуск скрипта

Для запуска скрипта пользователю нужно выполнить следующие действия

- Скачать с GitHub репозитория файл main.py в заранее подготовленное место
- Перейти в PowerShell(Windows)/Terminall(Linux/MacOs)
- Командой `cd path` , где path - абсолютный путь до файла main.py
- Запустить скрипт командой `python3 main.py`

## Работа со скриптом

- После запуска скрипта перед пользователем будет предложение ввести названия файла, в который будут сохраняться
  результаты выполнения кода
- Далее будет предложение ввести город, погоду которого необходимо узнать(на латинице)
- После этого в терминале отобразится информация о запрашиваемом городе, а также предложение продолжить/закончить работу

## Советы
1. При работе со скриптом на компьютер должен быть установлен python
2. Работа осуществляется только на английском языке


## Возможные ошибки
1. Ошибка работы с городом - данный город не найден/название города написано не в соответствии с БД API