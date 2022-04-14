<div align="center" style="padding-bottom: 10px">
    <h1>D2R Drop Tracker API</h1>
    <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray" alt=""/>
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/battle.net-%2300AEFF.svg?style=for-the-badge&logo=battle.net&logoColor=white" alt=""/>
</div>

<div align="center"></div>

## Tools, libraries, frameworks:

This setup has been tested on Python 3.9.6 and Django 4.0.3.

### Backend

## Development setup:

### Requirements:

- [Python](https://www.python.org/downloads/) 3.8+
- [pipenv](https://pypi.org/project/pipenv/)

### BattleNet API

Required for user authentication with BattleNet account.

1) Go to https://develop.battle.net/access/ and log into your BattleNet account
2) Create new API client
3) Provide client name, redirect url, intended use
4) Save Client ID and Client Secret and do not share them with anyone
5) Create .env file in projects directory with content:

```
BNET_CLIENT_ID=your_client_id_from_bnet_api
BNET_SECRET=your_secret_from_bnet_api
```

### Project setup

Install dependencies:

```shell
pipenv install
```

Run django application

```shell script
python manage.py runserver
```

Preparing (if there are any changes to db schema) and running migrations

```shell script
python manage.py makemigrations

python manage.py migrate
```

Create superuser

```shell script
python manage.py createsuperuser
```

### Running unit tests and coverage

Run tests using Coverage

```shell script
coverage run manage.py test
```

Get report from coverage:

```shell script
coverage report -m
```

## Todos

### Json files

- [x] Armor, Belts, Boots, Gloves, Helmets, Shields, Weapons, Class items - base items
- [x] Runes, gems, quest items
- [x] Sets
- [X] Set items
- [X] Unique items
- [ ] Statistics: Set items, unique items, Runewords
- [ ] Common magic items (skillers, jewels, small charms etc.)

#### Maybe

- [ ] Cube recipes
- [ ] Other miscellaneous items (arrows, potions, scrolls, non tradeable quest items)

### Characters management

- [ ] Equipment
- [ ] Mercenaries

### Items

- [ ] item's dimensions (width, height), optional descriptions, looks

### Item find

- [ ] ethereal item find

### Other

- [ ] description column in most of models
- [ ] modifiers (prefixes, suffixes), automods
- [ ] data validation (serializers, validators on models)
- [ ] better readme
- [ ] move qlvl from statistics to its own column (?)
