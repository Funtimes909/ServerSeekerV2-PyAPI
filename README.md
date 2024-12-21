[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Funtimes909/ServerSeekerV2-PyAPI)
[![Docker](https://img.shields.io/badge/Docker-%232496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=%232496ED)](https://hub.docker.com/r/nucceteere/serverseekerv2-pyapi)
[![FastAPI](https://img.shields.io/badge/FastAPI-%23009688?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=%23009688)](https://fastapi.tiangolo.com/)
[![Static Badge](https://img.shields.io/badge/Python-3.12-%233776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
![GitHub Last Commit](https://img.shields.io/github/last-commit/Funtimes909/ServerSeekerV2-PyAPI?style=for-the-badge&logo=github)
![GitHub Commit Activity](https://img.shields.io/github/commit-activity/w/Funtimes909/ServerSeekerV2-PyAPI?style=for-the-badge&logo=github)
![Code Size](https://img.shields.io/github/languages/code-size/Funtimes909/ServerSeekerV2-PyAPI?style=for-the-badge&logo=github)
![Lines of Code](https://img.shields.io/endpoint?style=for-the-badge&logo=github&url=https://ghloc.vercel.app/api/Funtimes909/ServerSeekerV2-PyAPI/badge?filter=.py$&label=lines%20of%20code&color=blue)


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

### Manual

#### Dev Server
The Dev Server allows for local, and only local access of the API, running on port 8000.

```bash
fastapi dev
```

#### Production

The production server should not be used alone.  
When deploying, a reverse proxy with a webserver like Apache, Nginx or Caddy (recommended) should be used.  
You should also deny connections to port 8000 from outside the network.  
The server runs on port 8000.  

```bash
fastapi run
```

### Docker

Create a file named `serverseekerv2.env` and fill it according to the `.env.example` file on the GitHub Repository.
When deploying, a reverse proxy with a webserver like Apache, Nginx or Caddy (recommended) should be used.  
You should also deny connections to port 8000 from outside the network.  
The server runs on port 8000.  

```bash
docker run --mount type=bind,src=./serverseekerv2.env,dst=/usr/src/app/.env -p 8000:8000 -d nucceteere/serverseekerv2-pyapi
```

## Special Thanks
- [@CuriousCodingCanadian](https://github.com/CuriousCodingCanadian) for bug fixes and improved docs
