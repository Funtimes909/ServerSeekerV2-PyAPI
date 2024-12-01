# ServerSeekerV2 Python API
ServerSeekerV2 API written in Python using FastAPI

## Requirements
A Postgres database that allows connections from localhost/outside depending on your setup.
Python 3.12 and up

## Installation

### Modules
```bash
python -m venv env
./env/bin/pip install -r ./requirements
```

### Postgres
Ubuntu/Debian:
```bash
sudo apt-get install postgresql
```
Arch:
```bash
sudo pacman -S postgresql
```

## Running

### Dev Server
You can only connect to this from localhost  
Runs on port 8000
```bash
fastapi dev
```

### Production
It is recommended that you reverse proxy with a webserver like Apache, Nginx or Caddy to the app.  
It is also recommended that you deny connections to port 8000 from outside.  
Runs on port 8000  
```bash
fastapi run
```
