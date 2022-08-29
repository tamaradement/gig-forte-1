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
## Data structure
### Objects:
- CustomUser
    - Username
    - Password
    - Email
    - First name
    - Last name
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
    - Tunes(Tune)
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
    - Call time
    - Start time
    - End time
    - Pay
    - Setlist(Setlist)
    - Personnel(CustomUser)
    - Accepts(CustomUser)
    - Declines(CustomUser)
### Relationships:
- Performer - Tune: OneToMany
    - A performer can have many tunes. 
    - A tune can belong to one performer.
- Performer - Setlist: OneToMany
    - A performer can have many setlists.
    - A setlist can belong to one performer.
- Tune - Setlist: ManyToMany
    - A tune can belong to many setlists.
    - A setlist can have many tunes. 
- Performer - Venue: OneToMany
    - A CustomUser can have many venues.
    - A venue can belong to one CustomUser.
- Gig - Bandleader: OneToMany
    - A bandleader can lead many gigs.
    - A gig has only one bandleader.
- Gig - Personnel/Accepts/Declines: ManyToMany
    - A gig can have many personnel/accepts/declines.
    - Personnel can be assigned to, accept or decline many gigs.
