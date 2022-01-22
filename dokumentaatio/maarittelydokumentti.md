## Harjoitustyö

Tehtävänä on toteuttaa sovellus millä voi sähköisesti allekirjoittaa asiakirjoja. Ajatuksena on että lähettäjä voi luoda asiakirjoja, joista muodostetaan tiiviste, jotka salataan ja allekirjoitetaan käyttäjän yksityisellä avaimella. Tämän jälkeen asiakirja ja lähettäjän julkinen avain voidaan toimittaa vastaanottajalle. Vastaanottaja voi tarkistaa että asiakirjan lähettäjä ja sisältö on säilynyt muuttumattomana käyttämällä lähettäjän julkista avainta. 

## Sovelluksen rakenne 

Sovellus toteutetaan Python kielellä. Salaukseen ja allekirjoittamisen käytetään RSA-salausta. RSA-salaus vaatii toimiakseen alkulukuja, ja erityisen isoja alkulukuja jotta salaus olisi turvallinen ja hankalasti murrettavissa. Isojen alkulukujen löytämiseen ja tarkistamiseen käytän Miller-Rabin-algoritmia.

Syötteenä sovellus saa lähettäjältä tekstiä mistä muodostetaan asiakirja. Asiakirjasta muodostetaan tiiviste joka salataan lähettäjän yksityisellä avaimella minkä jälken se lisätään asiakirjaan. Asiakirja ja lähettäjän julkinen avain toimitetaan vastaanottajalle. Vastaanottaja voi tarkistaa asiakirjan eheyden purkamalla tiiviste lähettäjän julkisella avaimella ja vertaamalla sitä dokumentin tiivisteeseen. 

Sovelluksen dokumentaatio ja kommentit ovat suomeksi ja sovelluksen muuttujat ja funktiot englanniksi. 

Miller-Rabin-algoritmin aikavaatimus on O(k log^3n) missä k on suoritettujen kierrosten määrä ja n on testattava luku. 

## Vertaisarviointi

Voin vertaisarvioida muita Python harjoitustöitä suomeksi sekä englanniksi. 


## Muuta

Valitsin kyseisen aiheen koska se kiinnostaa minua ja koska RSA-salaus on käytössä monessa arkisessa digipalvelussa.

Myös syvempi ymmärrys miksi RSA-salaus on suosittu, miksi se on turvallinen ja miten se on teknisesti toteutettu on myös mielenkiintoinen aihe.  

Suoritan tietojenkäsittelytieteiden kandidaatin tutkintoa.

## Lähteet

https://en.wikipedia.org/wiki/RSA_(cryptosystem)

https://fi.wikipedia.org/wiki/RSA

https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test