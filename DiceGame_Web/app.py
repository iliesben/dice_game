from flask import Flask
import controller.player_methods as Player_methods
import controller.game_methods as Game_methods
import controller.score_methods as Score_methods
import controller.dice_methods as Dice_methods
from models.player import Player
from models.game import Game

app = Flask(__name__)


@app.route('/')
def dice_game():
    test = Game_methods.launch_game()
    print(test)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
