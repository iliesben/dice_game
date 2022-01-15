import utils.constants as params
import utils.utils as utils
from models.dice import Dice


def analyse_standard_score(dice_value_occurrence_list):
    standard_score = 0
    for scoring_value, scoring_multiplier in zip(params.LIST_SCORING_DICE_VALUE, params.LIST_SCORING_MULTIPLIER):
        standard_score += dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
        dice_value_occurrence_list[scoring_value - 1] = 0
    return standard_score, dice_value_occurrence_list


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.best_scoring = 0
        self.nb_bonus_score = 0
        self.potential_score = 0
        self.nb_of_roll = 0
        self.nb_of_non_scoring_turn = 0
        self.non_potential_score = 0
        self.nb_of_full_roll = 0
        self.is_winning = False

    def launch_dice(self):
        roll = 0
        self.potential_score = 0
        dice_remaining = params.GAME_MAX_ROLL

        while dice_remaining > 0:
            response = utils.parse_to_str(input(self.name + " tap [y] or [yes] for roll dice! ")).lower()
            if response in ['y', 'yes']:
                score_turn = 0
                roll += 1
                dice = Dice()
                dice_value_occurrence_list = dice.roll_dice_set()
                scoring_dices = dice.scoring_dices()
                nbr_scoring_dice = dice.nbr_scoring_dices()
                self.nb_of_roll += 1
                score_turn = self.analyse_score(dice_value_occurrence_list)
                dice_remaining = dice_remaining - nbr_scoring_dice

                if dice_remaining < 0:
                    dice_remaining = 0

                print(
                    "Roll #" + utils.parse_to_str(roll) + " : " + utils.parse_to_str(nbr_scoring_dice)
                    + " scoring dices " + utils.parse_to_str(scoring_dices)
                    + " scoring " + utils.parse_to_str(score_turn)
                    + ", potential total turn score " + utils.parse_to_str(self.potential_score)
                    + ", remaining dice to roll : " + utils.parse_to_str(dice_remaining)
                )

                self.best_scoring = score_turn if score_turn > self.best_scoring else self.best_scoring

                if self.score + self.potential_score > params.DEFAULT_TARGET_SCORE:
                    return self.score, self.potential_score, roll




                # if self.potential_score >= params.DEFAULT_TARGET_SCORE:
                #     self.score = self.potential_score
                #     print('Test score : ', self.score)
                #     return self.score

            else:

                print("You win this turn, your score " + utils.parse_to_str(self.potential_score) + " pts")
                return self.score, self.potential_score, roll

            if dice_remaining < 1:
                self.nb_of_full_roll += 1
                return self.score, self.potential_score, roll

            if nbr_scoring_dice == 0:
                self.nb_of_non_scoring_turn += 1
                self.non_potential_score += self.potential_score
                print("You lose this turn and a potential to score "
                      + utils.parse_to_str(self.potential_score) + " pts")
                score_turn = 0
                return self.score, self.potential_score, roll

    def analyse_bonus_score(self, dice_value_occurrence_list):
        bonus_score = 0
        for side_value_index, dice_value_occurrence in enumerate(dice_value_occurrence_list):
            nb_of_bonus = dice_value_occurrence // params.THRESHOLD_BONUS
            if nb_of_bonus > 0:
                self.nb_bonus_score += 1
                if side_value_index == 0:
                    bonus_multiplier = params.BONUS_VALUE_FOR_ACE_BONUS
                else:
                    bonus_multiplier = params.BONUS_VALUE_FOR_NORMAL_BONUS
                bonus_score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)
                dice_value_occurrence_list[side_value_index] %= params.THRESHOLD_BONUS
        return bonus_score, dice_value_occurrence_list

    def analyse_score(self, dice_value_occurrence_list):
        score = 0
        bonus_score, dice_value_occurrence_list = self.analyse_bonus_score(dice_value_occurrence_list)
        standard_score, dice_value_occurrence_list = analyse_standard_score(dice_value_occurrence_list)
        score = bonus_score + standard_score
        self.potential_score = self.potential_score + score
        return score
