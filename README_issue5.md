# Запуск тестов

1. Откройте терминал и перейдите в директорию с файлом what_is_year_now.py.
2. Запустите тесты с помощью команды:

```bash
python -m unittest -v test_what_is_user_now.py
```
Чтобы сохранить в файл txt, необходимо:
```bash
python -m unittest -v test_what_is_user_now.py > result_test_what_is_user_now.txt
```

Убедившись, что у вас установлен pytest и coverage к нему, необходимо

```bash
python -m pytest -q test_what_is_year_now.py --cov=what_is_year_now
```

