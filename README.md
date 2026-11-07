# NP - Ivan Cvorovic

Ovaj repozitorijum služi za mini projekte i završni projekat u okviru kursa Napredno programiranje.

## Zadatak 1: Priprema radnog okruženja

### Korišćeni upit za AI asistenta:
> "Napiši mi Python funkciju pod nazivom `prosjecna_cijena` koja prima listu brojeva (cijena) i vraća njihov prosek. Funkcija treba da bude otporna na greške, odnosno da vrati 0.0 ako je lista prazna. Takođe, napiši Pytest testove za tu funkciju koji pokrivaju normalan slučaj, slučaj sa jednim elementom i praznu listu."

### Uočeni nedostaci generisanog koda:
* AI u početku nije uvijek stavio *type hinting* (`list[float] -> float`), što je dobra praksa u Pythonu.
* Inicijalna verzija testova koje je AI predložio nije testirala slučaj prazne liste, već je bacala `ZeroDivisionError`. Morao sam da dopunim prompt da bi AI dodao `if not cijene: return 0.0`.
* AI je predložio korišćenje `numpy.mean()` funkcije što zahtijeva dodatnu instalaciju biblioteke, pa sam ga zamolio da koristi ugrađene Python funkcije `sum()` i `len()` kako bi kod bio lakši i bez zavisnosti.

* ---

---

## Mini projekat 1: Refaktoring sistema za obdu rezervacija

Kao osnovu za ovaj mini projekat uzeo sam monolitni skript za obradu rezervacija i izvršio njegov refaktoring. Kompletan kod i testovi nalaze se u fajlu `np_ime_prezime.ipynb`.

### Proces rada i korišćeni AI prompt
Prilikom refaktoringa koristio sam AI asistenta kao pomoć za implementaciju SOLID principa. Inicijalni upit je bio:
> "Treba mi Python kod za obradu rezervacija. Molim te primeni principe Single Responsibility i Dependency Inversion. Koristi `typing.Protocol` za apstrakciju izvora podataka (Repository) i servisa za notifikacije. Takođe, obezbedi zamenske (fake) klase za testiranje i napiši najmanje 3 Pytest testa."

### Kritički osvrt na generisani kod (uočeni nedostaci i ispravke)
Nakon analize koda koji je AI generisao, uočio sam nekoliko stvari koje sam morao ručno da ispravim:
1. **Nedostatak apstrakcije:** AI je u prvoj iteraciji klasu `ObradaRezervacija` direktno vezao za konkretne klase, što krši Dependency Inversion. Ispravio sam to uvođenjem `Protocol` klasa (`RezervacijaRepository` i `NotifikacioniServis`) i dodavanjem *type hintinga* u konstruktor.
2. **Slabo pokriveni testovi:** Generisani testovi su pokrivali samo "srećan put" (happy path). Morao sam da dopunim testove tako što sam dodao proveru rada funkcije `generisi_izvjestaj()` na praznoj listi rezervacija, kako bih sprečio potencijalne greške u produkciji.
3. **Prilagođavanje okruženju (Colab):** Zbog povremenih nestabilnosti Google Colab servera i greške `Failed to fetch`, odlučio sam da izbegnem spoljne zavisnosti poput `pytest` biblioteke. Testove sam prilagodio da koriste ugrađene `assert` naredbe unutar obične Python funkcije, što omogućava da se testiranje izvrši bez ikakvih dodatnih instalacija.
