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

### Endpoints

`/api/pdf/` [POST] - Generate a PDF for download (see http://localhost:8000/api/pdf for list of POST parameters. There are a lot)
`/api/pdf/?url={REDFIN_SRC}` [GET] - Gets a PDF object by redfin_src URL
`/api/pdf/{id}/` [DELETE] - Markes a PDF object as "deleted"
`/api/search/` [POST] - Makes call to URL provided in request object. (see http://localhost:8000/api/search for POST parameters) 
