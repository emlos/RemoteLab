# praca z gitem

Każde zadanie: osobna gałąź -> pull request do `main` -> review jednej osoby -> **Squash and merge**. Głebsza rozpiska w [CONTRIBUTING.md](docs/CONTRIBUTING.md).

edycja schematu danych/dodawanie tabel kolumn etc - [rozpiska i tutorial w DATABASE.md](docs\DATABASE.md)

# instalacja

wymagainia: Python 3.14, PostgreSQL i powershell. instalacje zrob tylko przy **pierwszym** uruchomieniu na danym komputerze. git zapisuje tylko migracje opisujące strukturę bazy, dane jake dodasz beda tylko na twoim kompie

w ~konsoli~ linijka po linijce:

<details>
    <summary>PowerShell (klinknij)</summary>
    &nbsp

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```
</details>
&nbsp
<details>
    <summary>macOS (kliknij)</summary>
    &nbsp

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```
</details>

## instalacja postgres

1. [pobierz instalator](https://www.postgresql.org/download/windows/) i zainstaluj serwer postresql.

2. ustaw i zapamiętaj hasło użytkownika `postgres` (wpisz do .env, ponizej rozpisane); domyślny port to `5432`

3. otwórz pgAdmin, polacz się z lokalnym serwerem i stworz pustą bazę o nazwie `ipz` (`Databases` -> `Create` -> `Database`). nic innego nie musisz robic.

w idealnym swiecie bysmy uzywaly dockera...

## konfig dostepu pajtona do bazy

skopijuj zawarosc pliku `.env.example` do nowego pliku `.env`.

W `.env` zastąp `CHANGE_ME` hasłem użytkownika `postgres`.

np moje haslo to 12345678 wiec w .env ustawie:

```text
DATABASE_URL=postgresql://postgres:12345678@localhost:5432/ipz
```

nic wiecej nie musisz robic. tylko no zapisz plik xD

## skrypt do stworzenia sobie schematu bazy

po koleji:

<details>
    <summary>PowerShell (klinknij)</summary>
    &nbsp

```powershell
.\.venv\Scripts\python.exe -m alembic upgrade head
.\.venv\Scripts\python.exe -m alembic current
```
</details>
&nbsp
<details>
    <summary>macOS (kliknij)</summary>
    &nbsp

```bash
python3 -m alembic upgrade head
python3 -m alembic current
```
</details>
&nbsp

> **WAZNE:** po `git pull` uruchom ponownie `alembic upgrade head`. instalujesz tylko raz, upgrade head robisz po kazdym pullu!

# uruchamianie

<details>
    <summary>PowerShell (klinknij)</summary>
    &nbsp

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```
</details>
&nbsp
<details>
    <summary>macOS (kliknij)</summary>
    &nbsp

```bash
python3 -m uvicorn app.main:app --reload
```
</details>

- stronka na ktorej jest swerwowany ha-te-em-el: <http://127.0.0.1:8000/>
- Dokumentacja API: <http://127.0.0.1:8000/docs>

## przyklady api

#### GET

```powershell
$response = Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8000/api/v1/health"
$response.status
```

#### POST

```powershell
$body = @{
    name = "Test UX"
    config = @{ tasks = @("Znajdź przycisk") }
} | ConvertTo-Json -Depth 10

Invoke-RestMethod -Method Post `
    -Uri "http://127.0.0.1:8000/api/v1/experiments" `
    -ContentType "application/json; charset=utf-8" `
    -Body $body
```

btw nie lubisz powershella? zainstaluj [bruno](https://www.usebruno.com/) w ktorym masz edytor i wizualizacje api requestow.

...albo prosciej: jak serwer jest uruchomiony mozesz tu: <http://127.0.0.1:8000/docs>