from flask import Flask
import controller.player_methods as Player_methods
import controller.game_methods as Game_methods
import models.player as Player

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
