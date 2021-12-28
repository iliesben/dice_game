from random import random
import utils.constants as params
from models.player import Player
import controller.game_methods as game

# Lancer les dés
# Afficher le score
# Demander de relancer

def lost_roll(current_player, turn_score):
    # lost roll

    print('\n-->', Player.get_name(current_player), 'got zero point ', turn_score, 'lost points\n')

    # current_player['nb_of_non_scoring_turn'] += 1
    non_scoring_turn = Player.get_nb_of_non_scoring_turn(current_player)
    non_scoring_turn += 1
    # print(non_scoring_turn)

    # current_player['lost_score'] += turn_score
    lost_score = Player.get_lost_score(current_player)
    lost_score += turn_score
    # print(lost_score)
    
    roll_again = False

def scoring_roll(turn_score, roll_score):
    # scoring roll

    turn_score += roll_score['score']
    print('=> Scoring Dice', game.occurrence_list_to_str(roll_score['scoring_dice']),
            'for ', roll_score['score'], 'points',
            'total potential score :', turn_score)

def full_set_dice(remaining_dice_to_roll, current_player, roll_score):
    # In case of scoring roll and no remaining dice to roll the player can roll again the full set of dices
    remaining_dice_to_roll = params.DEFAULT_DICES_NB
    print('-->Full Roll')
    current_player['nb_of_full_roll'] += 1

    print('Non Scoring Dice ', game.occurrence_list_to_str(roll_score['non_scoring_dice']),
        "You can roll", remaining_dice_to_roll, "dices")

def stop_roll(current_player, turn_score):
    # stop turn and take roll score
    current_player['score'] += turn_score
    current_player['nb_of_scoring_turn'] += 1

    print('\n-->', current_player['name'], 'Scoring turn with', turn_score, 'points\n')

    roll_again = False

def game_turn(current_player, is_interactive=True):
    """ Handle a full player turn
        :parameters     current_player      dictionary of player information
                                            - 'name'
                                            - 'score'
                                            - 'lost_score'
                                            - 'nb_of_roll'
                                            - 'nb_of_turn'
                                            - 'nb_of_scoring_turn'
                                            - 'nb_of_non_scoring_turn'
                                            - 'nb_of_full_roll'
                        is_interactive      boolean for game mode
                                            - True -> interactive game mode
                                            - False -> random choice for game simulation
        :return:        updated dictionary of player information after a game turn
    """

    # turn start with the full set of dices
    remaining_dice_to_roll = params.DEFAULT_DICES_NB
    roll_again = True

    current_player['nb_of_turn'] += 1

    turn_score = 0
    while roll_again:
        # generate the dice roll and compute the scoring
        dice_value_occurrence = game.roll_dice_set(remaining_dice_to_roll)
        roll_score = game.analyse_score(dice_value_occurrence, current_player)
        remaining_dice_to_roll = sum(roll_score['non_scoring_dice'])
        current_player['nb_of_roll'] += 1

        if roll_score['score'] == 0:
            lost_roll(current_player, turn_score)
        else:
            scoring_roll(turn_score, roll_score)
            
            if remaining_dice_to_roll == 0:
                full_set_dice(remaining_dice_to_roll, current_player, roll_score)

            # choice to roll again or stop and take roll score
            if is_interactive:
                # interactive decision for real game
                stop_turn = input("Do you want to roll this dice ? [y/n] ") == "n"
            else:
                # random decision for game simulation (50/50)
                stop_turn = (random.randint(1, 100) % 2) == 0

            if stop_turn:
                stop_roll(current_player, turn_score)

    return current_player