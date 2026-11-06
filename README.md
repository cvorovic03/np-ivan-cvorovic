NP – Ime Prezime
Opis projekta

Projekat predstavlja implementaciju Python funkcije prosjecna_cijena, koja izračunava prosječnu cijenu na osnovu liste vrijednosti.

Korišćeni alati
Python 3.12
Google Colab
GitHub
Ruff
pytest
ChatGPT
Implementacija

Implementirana je funkcija prosjecna_cijena(cijene).

Funkcija računa aritmetičku sredinu elemenata liste. Ukoliko je lista prazna, podiže ValueError izuzetak.

Upotrijebljeni AI upit

"Uz AI asistenta implementirati funkciju prosjecna_cijena i priložiti test."

AI asistent je korišćen za generisanje početne implementacije funkcije i testova.

Uočeni nedostaci generisanog koda
Ne provjerava da li su svi elementi liste brojevi.
Nije definisano ponašanje za negativne cijene.
Nisu obrađeni svi slučajevi neispravnog ulaza.
Testovi pokrivaju osnovne slučajeve, ali ne sve moguće granične situacije.
Testiranje

Testiranje je izvršeno pomoću pytest biblioteke.

Testirani su:

Lista sa više cijena.
Lista sa jednom cijenom.
Prazna lista.
Zaključak

AI asistent je pomogao u implementaciji funkcije i pisanju testova. Generisani kod je provjeren pomoću pytest i Ruff alata.
