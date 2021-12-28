from flask import Flask
import controller.player_methods as Player_methods
import controller.game_methods as Game_methods
import controller.score_methods as Score_methods
import controller.dice_methods as Dice_methods
from models.player import Player
from models.game import Game

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # print(list(Player.__dict__.keys()))
    # player_one = Player("Julien")
    test = Game_methods.launch_game()
    print(test)
    # player_two = Player("Thomas")
    # turn_score_two = 0
    # test_2 = Player_methods.lost_roll(player_two, turn_score_two)
    # print(test_2)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
