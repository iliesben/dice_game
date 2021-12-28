from random import random
import utils.constants as params
from models.player import Player
import controller.score_methods as score
import controller.dice_methods as dice

# Lancer les dés
# Afficher le score
# Demander de relancer

def launch_dice(current_player, global_score):
    roll = 1
    potential_score = 0
    value = 0
    scoring = 0
    dice_remaining = params.GAME_MAX_ROLL
    nbr_scoring = 0
    global_current_score_player = 0
    while True:
        while dice_remaining > 0:
            response = input(Player.get_name(current_player) + " tap [y] or [yes] for roll dice! ").lower()
            if response in ['y', 'yes']:
                # global_score[name] = global_score[name] + score_final_turn if name in global_score else score_final_turn
                dice_value_occurrence_list = dice.roll_dice_set(params.DEFAULT_DICES_NB)
                scoring_dice = dice.scoring_dices(dice_value_occurrence_list)
                nbr_scoring = dice.nbr_scoring_dice(dice_value_occurrence_list)
                value = score.analyse_score(dice_value_occurrence_list, current_player)
                potential_score = potential_score + value[0]
                dice_remaining = dice_remaining - nbr_scoring
                scoring = value[0]
                # global_current_score_player = global_score[name] + scoring if name in global_score else scoring
                print(
                    "Roll #" + str(roll) + " : " + str(nbr_scoring)
                    + " scoring dices " + str(scoring_dice)
                    + " scoring " + str(scoring)
                    + ", potential total turn score " + str(potential_score)
                    + ", remaining dice to roll : " + str(dice_remaining)
                )
                roll = roll + 1
            else:
                print("You win this turn, your score " + str(potential_score) + " pts")
                return value, potential_score
            if dice_remaining < 1:
                return value, potential_score
            if nbr_scoring == 0:
                # print(display_scoring)
                print("You lose this turn and a potential to score " + str(potential_score) + " pts")
                value = 0
                return value, potential_score
        return value, potential_score