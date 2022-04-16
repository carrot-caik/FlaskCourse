# Flask Course
- Based off of following [this video](https://www.youtube.com/watch?v=Qr4QMBUPxWo) uploaded by freeCodeCamp.org.
- Current position in the video: 2:52:00 (Chapter: 9).

## Virtual Environment Setup
```bash
$ python3 -m venv .
# Get terminal into virtual environment
$ source ./bin/activate
# Install virtual environment packages
$ pip install flask flask-sqlalchemy flask-wtf wtforms
```

## Useful software
### Debian
```bash
$ sudo apt update
$ sudo apt install sqlitebrowser
```

### Arch
```bash
$ sudo pacman -Sy sqlitebrowser
```

## Environment Variables
```bash
$ export FLASK_APP=market.py
$ export FLASK_DEBUG=1
```

## Run Command
```bash 
$ flask run
```
