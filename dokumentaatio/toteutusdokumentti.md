# Toteutusdokumentti

## Yleisrakenne

Ohjelman on tarkoitus mahdollistaa digitaalinen allekirjoitus tiedoston datan perusteella. Tiedoston datasta luodaan tiiviste, joka allekirjoitetaan RSA-salauksen avulla. Kun tiedosto on allekirjoitettu, voidaan sen sisältö myöhemmin vahvistaa muuttumattomaksi ja alkuperäisen allekirjoittajan allekirjoittamaksi.

Alussa ohjelma pyytää tarvittavia tietoja käyttäjältä, joista luodaan allekirjoitettava tiedosto. Tiedoston datasta luodaan tiiviste, jonka avulla voidaan varmistaa jälkikäteen että tiedoston sisältö ei ole muuttunut. Tiiviste allekirjoitetaan RSA-salausta käyttäen. Jälkikäteen tiiviste voidaan purkaa samaa salausta käyttäen ja todeta kuka on tiedoston allekirjoittanut ja että tiedoston sisältö on säilynyt muuttumattomana.

Allekirjoitusta varten ohjelma luo satunnaisia alkulukuja joita voidaan käyttää RSA-salauksessa tarvittavien avaimien luomiseen. Kun alkuluvut on luotu, voidaan niistä laskea julkinen ja yksityinen avain. Yksityisellä avaimella allekirjoitetaan dokumentista luotu tiiviste ja julkisella avaimella voidaan varmistaa alkuperäinen allekirjoittaja. 

## Aika- ja tilavaativuudet

Alkulukujen löytämiseen käytetään Miller-Rabin algoritmia. Miller-Rabin algoritmin aikavaatimus on O(k log^3n) missä k on suoritettujen kierrosten määrä ja n on testattava luku. 

## Puutteet ja parannusehdotukset

## Lähteet

https://en.wikipedia.org/wiki/RSA_(cryptosystem)

https://fi.wikipedia.org/wiki/RSA

https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test