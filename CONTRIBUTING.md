# Praca zespołowa z GitHubem

Każde zadanie robimy na osobnej gałęzi. Zmiany trafiają do `main` przez pull request (PR) po zatwierdzeniu przez co najmniej jedną inną osobę.

## Rozpoczęcie zadania

W PowerShellu, w katalogu projektu:

```powershell
git switch main
git pull origin main
git switch -c feature/krotki-opis
```

Przykłady nazw: `feature/polaczenie-bazy`, `feature/strona-kalibracji`, `fix/formularz-badania`. Jedna gałąź powinna obejmować jedno zadanie.
W dalszych komendach zamień `feature/krotki-opis` na faktyczną nazwę swojej gałęzi.

## Wysłanie zmian

Sprawdź działanie swojej zmiany, a potem:

```powershell
git status
git add .
git commit -m "Dodaj stronę kalibracji"
git push -u origin feature/krotki-opis
```

Na GitHubie otwórz **Pull requests → New pull request**. Ustaw `base: main` i `compare: feature/krotki-opis`. Opisz zmianę i sposób sprawdzenia, a następnie poproś inną osobę z zespołu o review. Gdy PR ma zatwierdzenie i uwagi są rozwiązane, użyj **Squash and merge**. Autor PR nie zatwierdza własnej zmiany.

Po połączeniu zmian GitHub usuwa zdalną gałąź automatycznie. Przed kolejnym zadaniem zaktualizuj lokalne `main`:

```powershell
git switch main
git pull origin main
git branch -D feature/krotki-opis
```

Po **Squash and merge** Git może nie uznać lokalnej gałęzi za połączoną, dlatego usuń ją dopiero po sprawdzeniu, że PR jest zamknięty jako „Merged”.

Jeśli podczas pracy ktoś połączył inne zmiany z `main`, przed review zaktualizuj swoją gałąź:

```powershell
git fetch origin
git merge origin/main
```

W razie konfliktu popraw wskazane pliki, zapisz je, wykonaj `git add .`, `git commit`, a potem ponownie `git push`. Nie używaj `git push --force` na `main`.
