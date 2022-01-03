
import utils.constants as params
from models.player import Player
import controller.score_methods as score
import controller.dice_methods as dice


# Lancer les dés
# Afficher le score
# Demander de relancer

def launch_dice(current_player):
    roll = 1
    potential_score = 0
    scoring = 0
    dice_remaining = params.GAME_MAX_ROLL
    nbr_scoring = 0
    while dice_remaining > 0:
        response = input(Player.get_name(current_player) + " tap [y] or [yes] for roll dice! ").lower()
        if response in ['y', 'yes']:
            dice_value_occurrence_list = dice.roll_dice_set()
            scoring_dice = dice.scoring_dices(dice_value_occurrence_list)
            nbr_scoring = dice.nbr_scoring_dice(dice_value_occurrence_list)
            scoring = score.analyse_score(dice_value_occurrence_list, current_player)
            potential_score = potential_score + scoring
            dice_remaining = dice_remaining - nbr_scoring
            if dice_remaining < 0:
                dice_remaining = 0
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
            return scoring, potential_score
        if dice_remaining < 1:
            return scoring, potential_score
        if nbr_scoring == 0:
            # print(display_scoring)
            print("You lose this turn and a potential to score " + str(potential_score) + " pts")
            scoring = 0
            return scoring, potential_score