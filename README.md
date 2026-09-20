# nats-contracts

Pydantic-контракты сообщений между управляющим сервисом и ботами.

## Отправка тестовых сообщений

Из корня репозитория запускай `uv run scripts/send.py`. Нужны Python 3.14+
и `uv`; для отправки также нужен [NATS CLI](https://github.com/nats-io/natscli#installation)
(`nats` в PATH с поддержкой `--no-templates`).

Посмотреть готовое сообщение без подключения к NATS:

```bash
uv run scripts/send.py run-bot --bot-id bot-1 --dry-run
uv run scripts/send.py add-market --bot-id bot-1 --market-id 123 --dry-run
uv run scripts/send.py add-account --bot-id bot-1 --nickname test --wallet 0x123 --dry-run
```

Каждый запуск создаёт новые UUID для `message_id` и `trace_id`, ставит текущее
время в миллисекундах и проверяет сообщение по соответствующей модели.
Тип, имя и версия сообщения берутся из контракта. `--dry-run` выводит JSON
в stdout, а subject — в stderr, поэтому JSON можно сохранить через `> message.json`.

### Subject и подключение

Полный формат subject команд в этом репозитории не определён. Его нужно
указать через `--subject` либо настроить шаблон с `{bot_id}` и `{subject_suffix}`.
Без настройки subject доступен `--dry-run`: он покажет суффикс контракта.

Одноразовая отправка (замени `YOUR_FULL_SUBJECT` реальным subject):

```bash
uv run scripts/send.py run-bot --bot-id bot-1 --subject 'YOUR_FULL_SUBJECT'
```

Для коротких команд задай переменные в своей оболочке. Ниже **пример структуры
шаблона**, а не адрес из твоего сервиса: замени `YOUR_COMMAND_PREFIX` и при
необходимости порядок частей на формат, который слушает бот.

```bash
export NATS_BOT_ID='bot-1'
export NATS_COMMAND_SUBJECT_TEMPLATE='YOUR_COMMAND_PREFIX.{bot_id}.{subject_suffix}'

uv run scripts/send.py run-bot
uv run scripts/send.py add-market --market-id 123
uv run scripts/send.py add-account --nickname test --wallet 0x123
```

`--bot-id` переопределяет `NATS_BOT_ID`, `--subject-template` — переменную
шаблона, а `--subject` задаёт полный адрес вместо шаблона.
Суффиксы текущих команд:

| Команда | `{subject_suffix}` |
| --- | --- |
| `run-bot` | `V1.lifecycle.RunBotCommand` |
| `add-market` | `V1.trading_state.AddTrackingMarket` |
| `add-account` | `V1.state.AddAccountStateCommand` |

Подключение использует текущие настройки NATS CLI. Можно выбрать сохранённый
контекст (включая его авторизацию) или сервер:

```bash
uv run scripts/send.py run-bot --context dev
uv run scripts/send.py run-bot --server nats://localhost:4222
```

Это публикация через `nats pub`: скрипт не ждёт ответа бота.
Успешная публикация сама по себе не означает, что бот выполнил команду.

### Заготовки payload

В `examples/` лежат заготовки только полезной нагрузки; служебные поля
добавляются автоматически. Подставь свои тестовые значения, особенно wallet
в примере аккаунта.

```bash
uv run scripts/send.py add-market --bot-id bot-1 --payload-file examples/add_tracking_market.json --dry-run
uv run scripts/send.py add-account --bot-id bot-1 --payload-file examples/add_account_state.json --dry-run
```

Флаги переопределяют поля из файла:

```bash
uv run scripts/send.py add-market --bot-id bot-1 --payload-file examples/add_tracking_market.json --market-id 456 --dry-run
```

Для отправки убери `--dry-run` и настрой subject, как описано выше.
Отсутствующие обязательные поля, неизвестные ключи и ошибки JSON останавливают
скрипт до отправки. Справка: `uv run scripts/send.py add-market --help`.

## Тесты

```bash
uv run python -m unittest discover -s tests -v
```

Тесты проверяют сообщения и передачу данных подставному исполняемому файлу
`nats`; работающий сервер и установленный NATS CLI им не нужны.
