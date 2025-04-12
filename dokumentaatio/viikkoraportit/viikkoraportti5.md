# Viikkoraportti #5
## Mitä olen tehnyt tällä viikolla?
- Lisätty perustoteutus trie-tietorakenteesta simppeleine testeineen
- Lisätty toteutus toisen asteen  Markov chainista simppelien merkkipohjaisten testien kanssa. 
- Aloitettu varsinaisen datan käsittelyä tekemällä POC midi-tietostojen käsittelystä ja toistamisesta käyttäen Mido-kirjastoa

## Miten ohjelma on edistynyt?
Varsin hyvin vaikka toki ollaan aikataulusta pahasti jäljessä.

## Mitä opin tällä viikolla / tänään?
- Selkeni paljonkin miten ensimmäisen/toisen/kolmannen asteen Markov-ketjun toteutus käytännössä toimii. Ihan ei ollut vielä selvää aikaisemmin miten toimii, mutta kun pohti asiaa
trie:n ja käytettävissä olevan datan suhteen, niin johan alkoi aukeamaan.
- Pythonin Mido-kirjaston käyttäminen midi-tiedostojen prosessointiin vaati vähän ihmettelyä, mutta oikeastaan varsin simppeli systeemi. Tästä oli aikanaan jonkin verran keskustelua
opettajan kanssa. Ttosiaan formaattina nuo on tallennettu serial-formaatissa eli ne voidaan sinänsä prosessoida järjestyksessä. Ingest_midi.py tiedostossa on pieni prototyyppi jolla
ainakin leluesimerkit muutetaan monofoniseksi dataksi kiinteällä kestolla. Ajatuksena olisi että tarvittaessa tuota voi ainakin laajentaa niin, että yksittäisen nuotin kesto kvantifioidaan
kestämään "oikean keston" ja midi-tiedoston tempo/tick arvojen perusteella esim. arvoihin {1/16, 1/8, 1/4} jne. Tällöin periaatteessa markovin ketjulle annettava data voisi jo suoraan sisältää myös
nuotin keston varsinaisen nuotin lisäksi. Jos noita mahdollisia arvoja olisi esim. neljä, niin tämän lisäämisen ei pitäisi vielä ihan täysin räjäyttää mahdollisuuksian määrää.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Kunhan on päässyt varsinaisen tekemisen ääreen, niin hommat on edennyt melko kivuttomasti.

## Mitä teen seuraavaksi?
- Ohjelman varsinainen runko on jo valmiina. Seuraavaksi pitää vähän siistiä toteutusta ja toteuttaa mahdollisuus käyttää eri asteen Markov-ketjuja.
- Lisäksi pitää rakentaa jonkinsortin käyttöliittymä ja varsinkin testata erilaisilla midi-tiedostoilla miten tämä toimii.
- Puuttuu vielä mahdollisuus antaa dataksi enemmän kuin yhden midi-tiedoston yksi midi-raita

## Käytetty aika tällä viikolla
Noin 16h
