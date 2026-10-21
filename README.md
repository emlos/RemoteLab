
```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

docs (auto)<http://127.0.0.1:8000/docs>


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

