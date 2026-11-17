
# wymagania

python 3.14, windows powershell

# instalacja
w powershellu linijka po linijce
```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

# uruchomienie serwera python

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

docs (auto)<http://127.0.0.1:8000/docs>


# testowanie API przyklady

GET request z powershella
```powershell
$response = Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8000/api/v1/health"
$response.status
```

POST request z powershella
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

# co jeszcze trzeba zrobic w backendzie?

wejdz do tego pliku: [todo.md](TODO.md)

wybierz co robisz

jak skonczysz -> edytuj TODO.md i dodaj do zrobionych
s

# konfiguracja bazy danych postgresql
1. Instalacja PostgreSQL

Pobrac PostgreSQL ze strony https://www.postgresql.org/download/

Zainstalowac PostgreSQL wraz z pgAdmin4

Podczas instalacji ustawic haslo dla uzytkownika postgres i je zapamietac

2. Utworzyc baze danych

W pgAdmin4:

Polaczyc sie z lokalnym serwerem PostgreSQL

Prawym przyciskiem na Databases i create->database

Utworzyc baze danych

3. Utworzyc tabele

W bazie danych otworzyc Query Tool i w nim:
```
CREATE TABLE experiments (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    config JSONB NOT NULL
);
```

4. Plik .env

W glownym katalogu projektu utworzyc plik .env (.env ma być w gitignore) i w nim linijka:

DATABASE_URL=postgresql://postgres:TWOJE_HASLO@localhost:5432/NAZWA_BAZY_DANYCH

