import random
import operator
import utils.constants as params
from models.player import Player

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


def ranking_final_score(score_dict, index_turn):
  sort_score_dict = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)

  classment_score = ""
  for count, (player, score) in enumerate(sort_score_dict):
    if(count == 0):
      classment_score += player + " win ! scoring " + str(score) + "\n"
    else :
      classment_score += player + " lose ! scoring " + str(score) + "\n"

  print("Game in " + str(index_turn) + " turn(s)")
  print(classment_score)


def ranking(player):
    return dict(sorted(player.items(), key=lambda item: item["score"]))