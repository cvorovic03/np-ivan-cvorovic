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

## Mini projekat 1: Refaktoring obrade rezervacija

Kod za ovaj projekat nalazi se u nastavku iste Colab sveske (`np_ime_prezime.ipynb`).

### Korišćeni upiti za AI asistenta:
> "Napiši mi Python kod za obradu rezervacija. Želim da primenim SOLID principe (Single Responsibility i Dependency Inversion). Koristi `typing.Protocol` za izvor podataka i za slanje notifikacija. Zatim napiši zamenske (fake) klase za testiranje i najmanje 3 testa."

### Uočeni nedostaci i ispravke generisanog koda:
1. **Zavisnost od konkretnih klasa:** AI je u početku pisao `__init__(self, repo, notifikator)` bez tipova, što narušava Dependency Inversion. Ispravljeno je dodavanjem tipova `RezervacijaRepository` i `NotifikacioniServis` (Protokoli).
2. **Nedostatak testova za ivice:** AI je napisao testove samo za uspešno kreiranje rezervacije. Morao sam da tražim da doda test za generisanje izveštaja kada u bazi nema rezervacija (prazna lista), kako bih osigurao da funkcija ne baca grešku.
3. **Tehnički problemi sa Colab-om:** Zbog greške `Failed to fetch` na Google Colab serveru, testovi su prilagođeni da rade kao obične Python funkcije sa `assert` naredbama (umesto `pytest` biblioteke), kako bi se osiguralo da kod nesmetano prolazi u svakom okruženju.
