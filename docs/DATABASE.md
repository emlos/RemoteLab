# Zmiany schematu bazy danych

> **WAZNE**: NIE edytuj migracji, która została już uruchomiona lub udostępniona innym STWORZ KOLEJNA.

## Typowy przebieg

1. Utwórz plik migracji w głównym katalogu projektu:

   ```powershell
   .\.venv\Scripts\python.exe -m alembic revision -m "add experiment description"
   ```

   Alembic utworzy plik w `migrations/versions/` i sam wpisze `revision` oraz `down_revision`. Nie zmieniaj tych identyfikatorów. Samo `revision` **nie zmienia bazy**. W tym projekcie piszemy operacje ręcznie — nie używamy `--autogenerate`, bo nie mamy metadanych modeli SQLAlchemy.

2. Otwórz wygenerowany plik. W `upgrade()` wpisz zmianę, którą chcesz wykonać. przyklady nizej są fragmentami do umieszczenia **wewnątrz funkcji**

3. zastosuj migrację i sprawdź aktualną rewizję:

   ```powershell
   .\.venv\Scripts\python.exe -m alembic upgrade head
   .\.venv\Scripts\python.exe -m alembic current
   ```

4. jeżeli API czyta lub zapisuje zmienione pola, zaktualizuj też zapytania w `app/database.py` oraz modele i trasy w `app/routes/experiments.py`. i ofc commit i push do gita

> **WAZNE**: po git pull druga osoba uruchamia `alembic upgrade head` na swojej bazie.


## Cheat sheet

### Dodanie i usuwanie kolumny

```python
op.add_column("experiments", sa.Column("description", sa.Text(), nullable=True))

op.drop_column("experiments", "description")
```

### tworzenie i usuwanie

```python
op.create_table(
    "example_events",
    sa.Column("id", sa.BigInteger(), sa.Identity(always=True), primary_key=True),
    sa.Column("experiment_id", sa.BigInteger(), sa.ForeignKey("experiments.id"), nullable=False),
    sa.Column("data", postgresql.JSONB(), nullable=False),
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.text("CURRENT_TIMESTAMP"),
    ),
)
```
 `sa.Identity()` nadaje kolejne ID, `sa.ForeignKey()` laczy kolumnę z inną tabelą, a `JSONB` przechowuje JSON w PostgreSQL. `op.drop_table()` usuwa całą tabelę i dane

### Zmiana nazwy kolumny

```python
op.alter_column("experiments", "name", new_column_name="title")
```

### zmiana typu kolumny

```python
op.alter_column(
    "example_events",
    "experiment_id",
    existing_type=sa.Integer(),
    type_=sa.BigInteger(),
)
```

`existing_type` opisuje stary typ, `type_` nowy. Zmiana typu może się nie udać, jeśli istniejących danych nie da się przekonwertować.

### zmiana `NULL` na `NOT NULL`

```python
op.alter_column("experiments", "description", existing_type=sa.Text(), nullable=False)
```


### default value

```python
op.alter_column(
    "example_events",
    "created_at",
    existing_type=sa.DateTime(timezone=True),
    server_default=sa.text("CURRENT_TIMESTAMP"),
)

# usuniecie domyslnej warotsci:
op.alter_column("example_events", "created_at", server_default=None)
```


## Przydatne typy kolumn

| Składnia | Typowe zastosowanie |
| --- | --- |
| `sa.Text()` | Tekst bez ustalonego limitu |
| `sa.String(100)` | Tekst z limitem długości |
| `sa.Integer()` / `sa.BigInteger()` | Liczby całkowite |
| `sa.Boolean()` | `true` / `false` |
| `sa.Numeric(10, 2)` | Liczby dziesiętne, np. kwoty |
| `sa.Date()` | Data bez godziny |
| `sa.DateTime(timezone=True)` | Data i godzina ze strefą czasową; preferowane dla czasu zdarzeń |
| `postgresql.JSONB()` | Dane JSON w PostgreSQL |

Przykład dodania daty i czasu utworzenia, ustawianego przez bazę:

```python
op.add_column(
    "experiments",
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.text("CURRENT_TIMESTAMP"),
    ),
)
```