from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

games = [
    {
        "id": 1,
        "title": "Dungeons & Dragons 5e",
        "genre": "Fantasy",
        "players": "2-7"
    },
    {
        "id": 2,
        "title": "Call of Cthulhu",
        "genre": "Horror",
        "players": "2-6"
    }
]


@app.route("/")
def home():
    return {"message": "Welcome to the TTRPG Library API"}


@app.route("/games", methods=["GET"])
def get_games():
    return games


@app.route("/games", methods=["POST"])
def add_game():
    data = request.get_json()

    new_game = {
        "id": len(games) + 1,
        "title": data["title"],
        "genre": data["genre"],
        "players": data["players"]
    }

    games.append(new_game)

    return new_game, 201


if __name__ == "__main__":
    app.run(debug=True)