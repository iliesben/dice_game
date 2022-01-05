import utils.constants as params
# import controller.score_methods as score_methods
from models.dice import Dice

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        # self.bonus_score = 0
        # self.standard_score = 0
        self.lost_score = 0
        self.nb_of_roll = 0
        self.nb_of_turn = 0
        self.nb_of_scoring_turn = 0
        self.nb_of_non_scoring_turn = 0
        self.nb_of_potential_score = 0
        self.nb_of_full_roll = 0
        self.is_winning = False

    def launch_dice(self):
        # roll = 1
        # potential_score = 0
        # scoring = 0
        dice_remaining = params.GAME_MAX_ROLL
        # nbr_scoring = 0
        while dice_remaining > 0:
            response = input(self.name + " tap [y] or [yes] for roll dice! ").lower()
            if response in ['y', 'yes']:

                dice = Dice()
                dice_value_occurrence_list = dice.roll_dice_set()
                scoring_dices = dice.scoring_dices()
                nbr_scoring_dice = dice.nbr_scoring_dices()
                # print(dice)
                # print(scoring_dices)
                # print(str(nbr_scoring_dice))

                # dice_value_occurrence_list = Dice.roll_dice_set()
                # scoring_dice = Dice.scoring_dices(dice_value_occurrence_list)
                # nbr_scoring = Dice.nbr_scoring_dice(dice_value_occurrence_list)
                
                self.analyse_score(dice_value_occurrence_list)
                self.nb_of_potential_score = self.nb_of_potential_score + self.score
                dice_remaining = dice_remaining - nbr_scoring_dice
                if dice_remaining < 0:
                    dice_remaining = 0
                print(
                    "Roll #" + str(self.nb_of_roll) + " : " + str(nbr_scoring_dice)
                    + " scoring dices " + str(scoring_dices)
                    + " scoring " + str(self.score)
                    + ", potential total turn score " + str(self.nb_of_potential_score)
                    + ", remaining dice to roll : " + str(dice_remaining)
                )
                self.nb_of_roll += 1
            else:
                print("You win this turn, your score " + str(self.nb_of_potential_score) + " pts")
                return self.score, self.nb_of_potential_score
            if dice_remaining < 1:
                return self.score, self.nb_of_potential_score
            if nbr_scoring_dice == 0:
                # print(display_scoring)
                print("You lose this turn and a potential to score " + str(self.nb_of_potential_score) + " pts")
                self.score = 0
                return self.score, self.nb_of_potential_score

    def analyse_bonus_score(self, dice_value_occurrence_list):
        bonus_score = 0
        for side_value_index, dice_value_occurrence in enumerate(dice_value_occurrence_list):
            nb_of_bonus = dice_value_occurrence // params.THRESHOLD_BONUS
            if nb_of_bonus > 0:
                if side_value_index == 0:
                    bonus_multiplier = params.BONUS_VALUE_FOR_ACE_BONUS
                else:
                    bonus_multiplier = params.BONUS_VALUE_FOR_NORMAL_BONUS
                bonus_score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)
                dice_value_occurrence_list[side_value_index] %= params.THRESHOLD_BONUS
        # print('analyse bonus score ', self.bonus_score, dice_value_occurrence_list)
        return bonus_score, dice_value_occurrence_list

    def analyse_standard_score(self, dice_value_occurrence_list):
        standard_score = 0
        for scoring_value, scoring_multiplier in zip(params.LIST_SCORING_DICE_VALUE, params.LIST_SCORING_MULTIPLIER):
            standard_score += dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
            dice_value_occurrence_list[scoring_value - 1] = 0
        # print('analyse_standard_score: ', self.standard_score, dice_value_occurrence_list)
        return standard_score, dice_value_occurrence_list

    def analyse_score(self, dice_value_occurrence_list):
        bonus_score, dice_value_occurrence_list = self.analyse_bonus_score(dice_value_occurrence_list)
        standard_score, dice_value_occurrence_list = self.analyse_standard_score(dice_value_occurrence_list)
        self.score = bonus_score + standard_score

        print('analyse score: ', self.score)

        return self.score

    def get_name(self) -> str:
        return self.name

    def set_name(self, value):
        self.name = value

    def get_score(self) -> int:
        return self.score

    def set_score(self, value):
        self.score = value

    def get_lost_score(self) -> int:
        return self.lost_score

    def set_lost_score(self, value):
        self.lost_score = value

    def get_nb_of_roll(self) -> int:
        return self.nb_of_roll

    def set_nb_of_roll(self, value):
        self.nb_of_roll = value

    def get_nb_of_turn(self) -> int:
        return self.nb_of_turn

    def set_nb_of_turn(self, value):
        self.nb_of_turn = value

    def get_nb_of_scoring_turn(self) -> int:
        return self.nb_of_scoring_turn

    def set_nb_of_scoring_turn(self, value):
        self.nb_of_scoring_turn = value

    def get_nb_of_non_scoring_turn(self) -> int:
        return self.nb_of_non_scoring_turn

    def set_nb_of_non_scoring_turn(self, value):
        self.nb_of_non_scoring_turn = value

    def get_nb_of_full_roll(self) -> int:
        return self.nb_of_full_roll

    def set_nb_of_full_roll(self, value):
        self.nb_of_full_roll = value

    def is_winning(self) -> bool:
        return self.is_winning

    def is_winning(self, value):
        self.is_winning = value