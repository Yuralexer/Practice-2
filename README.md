# Ближе к делу
Перед началом необходимо установить uv:
```
pip install uv
```

Необходимо иметь руки, консоль и написать команду для установки зависимостей:
```bash
uv pip install -r pyproject.toml
```

Документацию (ТЗ) к каждой функции можно найти в файле **my_string/tools.py**

Запустить тесты:
```
uv run pytest -v .\my_string\tests.py
```

Запустить main.py:
```
uv run main.py
```
