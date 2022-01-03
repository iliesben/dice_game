import random
import utils.constants as params


def roll_dice_set():
    dice_value_occurrence_list = [0] * params.NB_DICE_SIDE
    for _ in range(params.DEFAULT_DICES_NB):
        dice_value = random.randint(1, params.NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value - 1] += 1
    return dice_value_occurrence_list


def scoring_dices(dice_value_occurrence_list):
    scoring_dice = []

    for dice_index, dice_value in enumerate(dice_value_occurrence_list):
        if (dice_value >= params.THRESHOLD_BONUS) or (dice_index + 1 in params.LIST_SCORING_DICE_VALUE and dice_value > 0) :
            scoring_dice += [(dice_value, dice_index + 1)]
    return scoring_dice


def nbr_scoring_dice(dice_value_list):
    nbr_scoring_dice = 0
    for scoring_value, scoring_multiplier in zip(params.LIST_SCORING_DICE_VALUE, params.LIST_SCORING_MULTIPLIER):
        if dice_value_list[scoring_value - 1] * scoring_multiplier > 0:
            nbr_scoring_dice += 1
    for side_value_index, dice_value_occurrence in enumerate(dice_value_list):
        nb_of_bonus = dice_value_occurrence // params.THRESHOLD_BONUS
        nbr_scoring_dice = nbr_scoring_dice + nb_of_bonus
    return nbr_scoring_dice
