# Автоматизация тестирования SauceDemo

Пять UI-тестов проверяют форму входа, успешную авторизацию, счётчик корзины, наличие Sauce Labs Backpack в корзине и сообщение об ошибке при неверном пароле. Нужен доступ к https://www.saucedemo.com/.

## Локальный запуск

Требуется Python 3.12. В корне проекта выполните:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v
```

В Windows PowerShell для активации используйте `.venv\Scripts\Activate.ps1`.

Запуск первого сценария отдельно:

```bash
python -m pytest -v test_login.py::test_login_page_is_displayed
```

## GitHub Actions

Workflow `Automated UI Tests` описан в `.github/workflows/tests.yml`. Он запускается при push, обновлении pull request и вручную, устанавливает Python 3.12, зависимости и Chromium, затем выполняет весь набор. Подробности прогона находятся в журнале шага `Run automated tests`.
