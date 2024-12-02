# ServerSeekerV2 Python API
ServerSeekerV2 API written in Python using FastAPI

## Requirements

A PostgreSQL database in the ServerSeekerV2 schema that allows connections from the API.  
Python 3.12+

## Installation

Clone the ServerSeekerV2 API Git repository
```bash
git clone https://github.com/Funtimes909/ServerSeekerV2-PyAPI
```
### Installing dependencies
The ServerSeekerV2 API depends on PostgreSQL and several Python libraries. These need to be installed to run the ServerSeekerV2 API.
  
#### Install Python requirements with pip
```bash
python -m venv env
./env/bin/pip install -r ./requirements
```

#### Install PostgreSQL
Debian (and derivatives):

```bash
sudo apt install postgresql
```

Arch (and derivatives):

```bash
sudo pacman -S postgresql
```

#### Install Git:

Ubuntu/Debian:

```bash
sudo apt-get install git
```

Arch:

```bash
sudo pacman -S git
```

## Running

### Dev Server
The Dev Server allows for local, and only local access of the API, running on port 8000.

```bash
fastapi dev
```

### Production

The production server should not be used alone.  
When deploying, a reverse proxy with a webserver like Apache, Nginx or Caddy should be used.  
You should also deny connections to port 8000 from outside the network.  
The server runs on port 8000.  

```bash
fastapi run
```

## Special Thanks
- [@CuriousCodingCanadian](https://github.com/CuriousCodingCanadian) for bug fixes and improved docs
