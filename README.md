# NP - Ivan Cvorovic

Ovaj repozitorijum služi za mini projekte i završni projekat u okviru kursa Napredno programiranje.

## Zadatak 1: Priprema radnog okruženja

### Korišćeni upit za AI asistenta:
> "Napiši mi Python funkciju pod nazivom `prosjecna_cijena` koja prima listu brojeva (cijena) i vraća njihov prosek. Funkcija treba da bude otporna na greške, odnosno da vrati 0.0 ako je lista prazna. Takođe, napiši Pytest testove za tu funkciju koji pokrivaju normalan slučaj, slučaj sa jednim elementom i praznu listu."

### Uočeni nedostaci generisanog koda:
* AI u početku nije uvijek stavio *type hinting* (`list[float] -> float`), što je dobra praksa u Pythonu.
* Inicijalna verzija testova koje je AI predložio nije testirala slučaj prazne liste, već je bacala `ZeroDivisionError`. Morao sam da dopunim prompt da bi AI dodao `if not cijene: return 0.0`.
* AI je predložio korišćenje `numpy.mean()` funkcije što zahtijeva dodatnu instalaciju biblioteke, pa sam ga zamolio da koristi ugrađene Python funkcije `sum()` i `len()` kako bi kod bio lakši i bez zavisnosti.
