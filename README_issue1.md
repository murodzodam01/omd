# Запуск тестов

1. Откройте терминал и перейдите в директорию с файлом morse.py.
2. Запустите тесты с помощью команды:

```bash
python -m doctest -v -o NORMALIZE_WHITESPACE test_encode_morse_doctest.py
```
Чтобы сохранить в файл txt, необходимо:
```bash
python -m doctest -v -o NORMALIZE_WHITESPACE test_encode_morse_doctest.py > result_encode_morse_doctest.txt
```
