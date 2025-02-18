# Модели ответов

В этом задании вам предстоит создать FastAPI приложение для управления списком продуктов. Все запросы на получение списка продуктов должны использовать модели ответов (response models), чтобы определять, какие данные будут возвращены клиенту. Модели ответов позволяют нам точно описывать формат ответа, улучшая читаемость и безопасность.

## src/main.py

- Маршрут POST `/product`:
    - Должен принимать данные о продукте, такие как название, цена и характеристики. Продукт добавляется в список.
    - Важно: модель продукта должна содержать валидацию, чтобы цена была больше нуля.
- Маршрут GET `/products`:
    - Этот маршрут должен возвращать список всех продуктов. Однако при этом будет использована модель ответа, которая будет включать только необходимые поля (например, name и price), игнорируя лишнюю информацию.
- Маршрут GET `/product/{product_id}`:
    - Этот маршрут должен возвращать информацию о конкретном продукте по его уникальному идентификатору. Также следует использовать модель ответа, которая будет включать только нужные поля продукта.

Описание моделей:

- `Product`:
    - Модель, которая представляет продукт, включая его название, цену и характеристики.
    - Характеристики должны быть вложенной моделью с полями: `size`, `color`, `material`.
- `ProductResponse`:
    - Модель ответа, которая будет использоваться для маршрута `/products`. Эта модель будет включать только поля `id`, `name`, и `price`.
- `ProductDetailResponse`:
    - Модель ответа, которая будет использоваться для маршрута `/product/{product_id}`. Эта модель будет включать поля `id`, `name`, `price`, а также все характеристики продукта.