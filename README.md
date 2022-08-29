# GigForte (aka tunes-1)
A productivity app for musicians, small ensembles and bandleaders.
## Setup
- First, clone the repository:
```sh
% git clone https://github.com/tamaradement/tunes-1.git
% cd tunes-1
```
- Create a virtual environment to install dependencies in and activate it.
```sh
% python3 -m venv .venv
% source .venv/bin/activate
(.venv) %
```
- Then install the dependencies.
```sh
% pip install -r requirements.txt
```
- Once `pip` has finished, spin up the server.
```sh
% python manage.py runserver
```
## How to use the app:
- [Add a tune](https://www.loom.com/share/8f0b57a0ad6848a88a633aff4035a891)
- [Create a setlist](https://www.loom.com/share/5b9be8825d394aeb8b935461f87abad5)
- [Add venues](https://www.loom.com/share/5b32ac6467204c6d879f803b852b6776)
- [Create a gig](https://www.loom.com/share/eaf8be7335e94519983823930639fc33)
- [Accept / Decline form](https://www.loom.com/share/432ac36fb0364a7c836f601e65eccf06)
## Data structure:
- CustomUser
    - Instrument
- Tune
    - Title
    - Composer
    - Key
    - Notes
    - Genre
    - PDF
    - Performer(CustomUser)
- Setlist
    - Title
    - Performer(CustomUser)
    - Description
    - Tunes(Tune, ManyToMany)
- Venue
    - Name
    - Address 1
    - Address 2
    - City
    - State
    - Zip
    - Website
    - Performer(CustomUser)
- Gig
    - Title
    - Created
    - Event date
    - Bandleader(CustomUser)
        - A gig has one bandleader, and a bandleader can lead many gigs.
    - Call time
    - Start time
    - End time
    - Pay
    - Setlist(Setlist, OneToMany)
        - A gig can have one setlist, and setlist can belong to many gigs.
    - Personnel(CustomUser, ManyToMany)
    - Accepts(CustomUser, ManyToMany)
    - Declines(CustomUser, ManyToMany)