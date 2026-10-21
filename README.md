
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
