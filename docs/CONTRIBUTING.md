# Praca zespołowa z GitHubem

>Każdy feature robimy na osobnej gałęzi. Zmiany trafiają do `main` przez pull request (PR) po zatwierdzeniu przez co najmniej jedną inną osobę.

## Rozpoczęcie zadania

Jak wiesz nad czym chcesz pracowac to:
1. wroc do maina
2. pobierz najnowsze zmiany
3. stworz nowego brancha dla twojego ficzura

```powershell
git checkout main
git pull origin main
git checkout -b feature/krotki-opis
```

>Przykłady nazw: `feature/polaczenie-bazy`, `feature/strona-kalibracji`, `fix/formularz-badania`. Jedna gałąź powinna obejmować jedno zadanie.


## Wysłanie zmian

**SPRAWDZ CZY DZIALA** a potem:

```powershell
git add .
git commit -m "opis twojej zmiany, nie rozpisuj sie"
git push -u origin feature/krotki-opis
```

potem, [wejdz na strone repozytorium](https://github.com/emlos/RemoteLab)

na GH otwórz **Pull requests → New pull request**. Ustaw `base: main` i `compare: feature/krotki-opis`. Opisz zmianę i sposób sprawdzenia, a następnie poproś inną osobę z zespołu o review. Gdy PR ma zatwierdzenie i uwagi są rozwiązane, użyj **Squash and merge**. Autor PR nie zatwierdza własnej zmiany.

## jesli sa konflikty albo ktos zmergował PRa zanim ty to zrobiłas

Zaktualizuj swoją gałąź zanim ktos inny zatwierdzi + zmergue twoj merge review.

zakładając ze jestes na branchu `feature/cos-nowego`

```powershell
git fetch origin
git merge origin/main
```

>W razie konfliktu popraw wskazane pliki, zapisz je, wykonaj `git add .`, `git commit`, a potem ponownie `git push`. git push na koniec jest **bardzo** wazne.

a w razie problemow to pykaj do mnie kochana ja ci zalatwie niebo i ziemie no i wsyztsko

#
podpisano, <br>
wasz #Admin
