from flask import Flask,render_template,request

import controller.player_methods as Player_methods
import controller.game_methods as Game_methods
import controller.score_methods as Score_methods
from models.player import Player
from models.game import Game
from models.dice import Dice

app = Flask(__name__)


@app.route('/launch')
def dice_game():

#     """
#     DICE MODELS
#     """
#     # dice = Dice()
#     # dice.roll_dice_set()
#     # scoring_dices = dice.scoring_dices()
#     # nbr_scoring_dice = dice.nbr_scoring_dices()
#     # print(dice)
#     # print(scoring_dices)
#     # print(str(nbr_scoring_dice))

#     """
#     PLAYER MODELS
#     """
#     # player = Player("Julien")
#     # player.analyse_bonus_score([0,1,1,3,0,0])
#     # player.analyse_standard_score([1,1,1,1,1,0])
    
#     # player.launch_dice()
#     # print(player)

    """
    GAME MODELS
    """
    game = Game()
    game.launch_game()

    return  'eee'



@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/setPlayer', methods=['POST'])
def numberplayer():
                    player_list = request.json.get("player_list")
                    game = Game()
                    game.launch_game(player_list)
                    return  'eee'

                    # launchGame =  Game_methods.launch_game(player_list)
                    # return launchGame


if __name__ == '__main__':
    app.run()


