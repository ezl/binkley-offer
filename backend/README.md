# Local Setup

### Dependencies

- Python 3
- Pipenv
- Django (DRF)
- PostgreSQL

### Local Install

Before running the setup commands, make sure that PostgreSQL is setup and running on your local machine. Edit `envs/local.env` with the Postgres credential of your local machine.

1. `source envs/local.env`
2. `pipenv install`
3. `make migrate`
4. `make start` 

`make test` will run unit tests for all endpoints. 
