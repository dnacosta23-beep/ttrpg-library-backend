# TTRPG Library Backend

## What This Project Does

This Flask application serves as the backend API for the TTRPG Library project. It stores a list of tabletop role-playing games and provides endpoints to retrieve all games and add new games.

The game data is currently stored in memory using a Python list of dictionaries.

## Requirements

- Python 3
- Flask
- Flask-CORS

## Installation

Install the required packages:

```bash
pip3 install flask flask-cors
```

## Running the Backend

Start the Flask server:

```bash
python3 app.py
```

The API will run at:

```
http://127.0.0.1:5000
```

## Available Routes

### GET /games

Returns all games in the library.

### POST /games

Adds a new game to the library.