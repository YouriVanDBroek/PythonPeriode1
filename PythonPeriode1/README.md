# Werken met deze GitHub repository

In deze repository staan de opdrachten voor de lessen.

Voor iedere week wordt een **aparte branch** gemaakt, bijvoorbeeld:

* `week-01`
* `week-02`
* `week-03`

Je maakt eerst een **fork** van deze repository. Daarna werk je vanuit je eigen GitHub-account verder.

Je levert je werk dus niet rechtstreeks in op de repository van de docent.

---

# 1. Repository forken

Ga op GitHub naar de repository van de docent.

Klik rechtsboven op:

**Fork**

GitHub maakt nu een kopie van de repository onder jouw eigen GitHub-account.

Bijvoorbeeld:

Repository van de docent:

```text
docent/python-opdrachten
```

Jouw fork:

```text
jouwnaam/python-opdrachten
```

Je kunt nu wijzigingen maken zonder de repository van de docent aan te passen.

---

# 2. Je eigen repository clonen

Nu gaan we jouw fork downloaden naar je computer.

Open een terminal in de map waarin je het project wilt opslaan.

Gebruik:

```bash
git clone https://github.com/JOUW-GITHUB-NAAM/python-opdrachten.git
```

Ga daarna naar de map:

```bash
cd python-opdrachten
```

## Wat doet `git clone`?

`git clone` maakt een lokale kopie van een GitHub repository op jouw computer.

Je kunt daarna bestanden aanpassen, commits maken en deze weer naar GitHub sturen.

---

# 3. De repository van de docent toevoegen

Jouw eigen GitHub repository wordt automatisch `origin` genoemd.

We voegen daarnaast de repository van de docent toe. Deze noemen we `upstream`.

Gebruik:

```bash
git remote add upstream URL-VAN-DE-REPOSITORY-VAN-DE-DOCENT
```

Bijvoorbeeld:

```bash
git remote add upstream https://github.com/docent/python-opdrachten.git
```

Je kunt controleren welke repositories gekoppeld zijn met:

```bash
git remote -v
```

Je ziet dan ongeveer:

```text
origin    https://github.com/jouwnaam/python-opdrachten.git
upstream  https://github.com/docent/python-opdrachten.git
```

## Wat betekenen `origin` en `upstream`?

**origin**

Dit is jouw eigen GitHub repository.

Hier stuur je jouw gemaakte opdrachten naartoe.

**upstream**

Dit is de repository van de docent.

Hier haal je nieuwe opdrachten en nieuwe branches vandaan.

Kort samengevat:

```text
Docent repository
      |
      | upstream
      v
Jouw computer
      |
      | origin
      v
Jouw GitHub repository
```

---

# 4. Controleren op welke branch je zit

Gebruik:

```bash
git branch
```

Je ziet bijvoorbeeld:

```text
* main
```

Het sterretje geeft aan op welke branch je momenteel werkt.

Je kunt ook gebruiken:

```bash
git status
```

Hiermee zie je onder andere:

* op welke branch je zit;
* welke bestanden zijn aangepast;
* welke bestanden klaarstaan voor een commit.

---

# 5. Een nieuwe week ophalen

Voor iedere week maakt de docent een nieuwe branch.

Bijvoorbeeld:

```text
week-01
week-02
week-03
week-04
```

Voordat je aan een nieuwe week begint, moet je eerst de nieuwste informatie van de repository van de docent ophalen.

Gebruik:

```bash
git fetch upstream
```

## Wat doet `git fetch`?

`git fetch` controleert de repository van de docent en haalt informatie over nieuwe commits en branches op.

Je bestanden worden hierdoor nog niet aangepast.

Je computer weet na `fetch` bijvoorbeeld dat er een nieuwe branch bestaat:

```text
upstream/week-04
```

---

# 6. De branch van de nieuwe week aanmaken

Stel dat de docent de branch `week-04` heeft toegevoegd.

Gebruik dan:

```bash
git switch -c week-04 upstream/week-04
```

Hiermee gebeurt het volgende:

1. Git zoekt de branch `upstream/week-04`.
2. Git maakt op jouw computer een eigen branch genaamd `week-04`.
3. Je schakelt direct over naar deze branch.

Controleer dit met:

```bash
git branch
```

Je ziet bijvoorbeeld:

```text
main
* week-04
```

Je werkt nu op `week-04`.

---

# 7. De branch naar je eigen GitHub sturen

De branch bestaat nu alleen nog op jouw computer.

Stuur hem daarom naar jouw eigen GitHub repository:

```bash
git push -u origin week-04
```

## Wat doet `git push`?

`git push` stuurt jouw lokale commits naar GitHub.

Met:

```bash
-u origin week-04
```

vertel je Git dat jouw lokale `week-04` gekoppeld moet worden aan `week-04` op jouw eigen GitHub repository.

Hierna kun je meestal gewoon gebruiken:

```bash
git push
```

---

# 8. Werken aan de opdracht

Je kunt nu aan de opdrachten van de week werken.

Controleer regelmatig:

```bash
git status
```

Hiermee kun je zien welke bestanden je hebt aangepast.

---

# 9. Bestanden toevoegen aan een commit

Wanneer je een bestand hebt aangepast, moet je Git eerst vertellen welke wijzigingen je wilt opslaan.

Gebruik:

```bash
git add .
```

## Wat doet `git add`?

`git add` zet wijzigingen klaar voor de volgende commit.

De punt:

```text
.
```

betekent dat alle gewijzigde bestanden in de huidige map worden toegevoegd.

Je kunt ook één bestand toevoegen:

```bash
git add opdracht1.py
```

---

# 10. Een commit maken

Wanneer je bestanden met `git add` hebt toegevoegd, kun je een commit maken.

Gebruik:

```bash
git commit -m "Opdracht 1 gemaakt"
```

Bijvoorbeeld:

```bash
git commit -m "Opdrachten week 4 afgerond"
```

## Wat is een commit?

Een commit is een opgeslagen versie van jouw project.

Je kunt het zien als een soort controlepunt.

Iedere commit bevat:

* jouw wijzigingen;
* jouw naam;
* de datum;
* een beschrijving van wat je hebt aangepast.

Gebruik duidelijke commitberichten.

Goed:

```text
Opdracht 2 while-loop gemaakt
```

Minder goed:

```text
ding aangepast
```

---

# 11. Je commits naar GitHub sturen

Een commit staat eerst alleen op jouw eigen computer.

Gebruik:

```bash
git push
```

Hiermee stuur je jouw commits naar jouw eigen GitHub repository.

De volgorde is dus meestal:

```bash
git add .
git commit -m "Beschrijving van mijn wijzigingen"
git push
```

---

# 12. Wijzigingen ophalen met `git pull`

Soms staat er op GitHub een nieuwere versie van jouw branch dan op jouw computer.

Gebruik dan:

```bash
git pull
```

## Wat doet `git pull`?

`git pull` haalt nieuwe commits op en probeert deze direct samen te voegen met jouw lokale branch.

Eigenlijk doet `git pull` ongeveer twee dingen:

```text
git fetch
+
git merge
```

Gebruik `git pull` bijvoorbeeld wanneer je op meerdere computers aan dezelfde repository werkt.

---

# 13. Nieuwe wijzigingen van de docent ophalen

Het kan gebeuren dat de docent tijdens een week een opdracht aanpast.

Je kunt eerst de nieuwste wijzigingen ophalen:

```bash
git fetch upstream
```

Stel dat je werkt op:

```text
week-04
```

Controleer eerst of je daadwerkelijk op die branch zit:

```bash
git switch week-04
```

Daarna kun je de veranderingen van de docent samenvoegen met jouw branch:

```bash
git merge upstream/week-04
```

## Wat doet `git merge`?

`git merge` voegt twee versies van een branch samen.

In dit geval:

```text
upstream/week-04
```

is de versie van de docent.

En:

```text
week-04
```

is jouw eigen versie.

Git probeert de wijzigingen automatisch samen te voegen.

Daarna kun je de nieuwe versie naar je eigen GitHub sturen:

```bash
git push
```

---

# 14. Merge conflicts

Soms hebben jij en de docent hetzelfde stukje van hetzelfde bestand aangepast.

Git weet dan niet automatisch welke versie gebruikt moet worden.

Dit noemen we een:

**merge conflict**

Je ziet bijvoorbeeld iets als:

```text
<<<<<<< HEAD

jouw code

=======

code van de docent

>>>>>>> upstream/week-04
```

Je moet dan zelf bepalen welke code je wilt bewaren.

Verwijder daarna de regels:

```text
<<<<<<<
=======
>>>>>>>
```

Sla het bestand op.

Gebruik vervolgens:

```bash
git add .
```

En maak een commit:

```bash
git commit -m "Merge conflict opgelost"
```

Daarna:

```bash
git push
```

---

# 15. Wisselen tussen weken

Je kunt tussen branches wisselen met:

```bash
git switch NAAM-VAN-DE-BRANCH
```

Bijvoorbeeld:

```bash
git switch week-03
```

of:

```bash
git switch week-04
```

Bekijk alle lokale branches met:

```bash
git branch
```

Bekijk ook branches die je via GitHub hebt opgehaald met:

```bash
git branch -a
```

---

# 16. Belangrijk: werk altijd op de juiste week-branch

Werk niet aan opdrachten op de `main` branch.

Gebruik altijd de branch die hoort bij de betreffende week.

Dus:

```text
week-01 → opdrachten van week 1
week-02 → opdrachten van week 2
week-03 → opdrachten van week 3
```

Controleer voordat je begint altijd:

```bash
git status
```

of:

```bash
git branch
```

Zo voorkom je dat je opdrachten op de verkeerde branch maakt.

---

# Stappenplan voor een nieuwe week

Wanneer er een nieuwe week beschikbaar is, voer je het volgende uit.

Stel dat de nieuwe branch `week-05` heet:

```bash
git fetch upstream
git switch -c week-05 upstream/week-05
git push -u origin week-05
```

Daarna kun je beginnen met de opdrachten.

Wanneer je klaar bent:

```bash
git add .
git commit -m "Opdrachten week 5 gemaakt"
git push
```

---

# Stappenplan wanneer de docent iets heeft aangepast

Ga eerst naar de juiste branch:

```bash
git switch week-05
```

Haal de nieuwste informatie op:

```bash
git fetch upstream
```

Voeg de wijzigingen van de docent samen met jouw werk:

```bash
git merge upstream/week-05
```

Stuur daarna jouw bijgewerkte branch naar GitHub:

```bash
git push
```

---

# Overzicht van belangrijke commando's

| Commando                                     | Betekenis                                                          |
| -------------------------------------------- | ------------------------------------------------------------------ |
| `git clone URL`                              | Downloadt een repository naar je computer                          |
| `git status`                                 | Laat zien op welke branch je zit en welke bestanden gewijzigd zijn |
| `git branch`                                 | Laat jouw lokale branches zien                                     |
| `git branch -a`                              | Laat lokale en remote branches zien                                |
| `git switch branchnaam`                      | Wisselt naar een andere branch                                     |
| `git switch -c branchnaam remote/branchnaam` | Maakt een lokale branch vanaf een remote branch                    |
| `git remote -v`                              | Laat gekoppelde GitHub repositories zien                           |
| `git remote add upstream URL`                | Koppelt de repository van de docent                                |
| `git fetch upstream`                         | Haalt nieuwe informatie van de docent op                           |
| `git add .`                                  | Zet alle wijzigingen klaar voor een commit                         |
| `git commit -m "bericht"`                    | Maakt een opgeslagen versie van je wijzigingen                     |
| `git push`                                   | Stuurt commits naar jouw GitHub                                    |
| `git pull`                                   | Haalt wijzigingen op en voegt ze samen                             |
| `git merge branchnaam`                       | Voegt een andere branch samen met jouw huidige branch              |

---

# De belangrijkste workflow

Tijdens het maken van opdrachten zul je vooral deze commando's gebruiken:

```bash
git status
git add .
git commit -m "Beschrijving van mijn wijzigingen"
git push
```

Bij een nieuwe week gebruik je:

```bash
git fetch upstream
git switch -c week-XX upstream/week-XX
git push -u origin week-XX
```

Wanneer de docent iets heeft aangepast:

```bash
git switch week-XX
git fetch upstream
git merge upstream/week-XX
git push
```

Controleer vooral altijd voordat je begint of je op de juiste branch zit:

```bash
git status
```
