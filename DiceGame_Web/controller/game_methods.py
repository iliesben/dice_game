import random
import utils.constants as params
from models.player import Player


def add_player():
    number_of_players = int(input("Enter number of players:\n", ))
    player_list = []
    for _ in range(number_of_players):
        name_player: str = input("Enter your name:\n", )
        player_list.append(Player(name_player))
    return player_list


def roll_dice_set(player):
    print(f"{player.name} roll dice")
    dice_value_occurrence_list = [0] * params.NB_DICE_SIDE
    for _ in range(params.DEFAULT_DICES_NB):
        dice_value = random.randint(1, params.NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value - 1] += 1
    return dice_value_occurrence_list


def analyse_bonus_score(dice_value_occurrence_list):
    score = 0
    for side_value_index, dice_value_occurrence in enumerate(dice_value_occurrence_list):
        nb_of_bonus = dice_value_occurrence // params.THRESHOLD_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0:
                bonus_multiplier = params.BONUS_VALUE_FOR_ACE_BONUS
            else:
                bonus_multiplier = params.BONUS_VALUE_FOR_NORMAL_BONUS
            score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)
            dice_value_occurrence_list[side_value_index] %= params.THRESHOLD_BONUS

    return score, dice_value_occurrence_list


def analyse_standard_score(dice_value_occurrence_list):
    score = 0
    for scoring_value, scoring_multiplier in zip(params.LIST_SCORING_DICE_VALUE, params.LIST_SCORING_MULTIPLIER):
        score += dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
        dice_value_occurrence_list[scoring_value - 1] = 0

    return score, dice_value_occurrence_list


def analyse_score(dice_value_occurrence_list, player):
    bonus_score, dice_value_occurrence_list = analyse_bonus_score(dice_value_occurrence_list)
    standard_score, dice_value_occurrence_list = analyse_standard_score(dice_value_occurrence_list)
    player.score = bonus_score + standard_score

    return bonus_score + standard_score, dice_value_occurrence_list

def ranking(player):
    return dict(sorted(player.items(), key=lambda item: item["score"]))

def occurrence_list_to_str(dice_value_occurrence):
    """ convert dice occurrence in string
            :parameters dice_value_occurrence
            :returns    string in format [Dice Side]xNb of Occurrence
    """

    if sum(dice_value_occurrence) == 0:
        # no occurrence for all dice value
        return '[]'

    occurrence_str = ''
    for side_value_index, side_value_occurrence in enumerate(dice_value_occurrence):
        if side_value_occurrence > 0:
            occurrence_str += '[' + str(side_value_index + 1) + ']' + 'x' + str(side_value_occurrence) + ', '

    return occurrence_str