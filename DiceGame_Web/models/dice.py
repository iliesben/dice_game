import random
import utils.constants as params

class Dice:

    dice_value:int

    def __init__(self):
        self.dice_value = 0
        self.dice_value_occurrence_list = []
        self.scoring_dice = []
        self.nbr_scoring_dice = 0

    
    def roll_dice_set(self):
        self.dice_value_occurrence_list = [0] * params.NB_DICE_SIDE
        for _ in range(params.DEFAULT_DICES_NB):
            self.dice_value = random.randint(1, params.NB_DICE_SIDE)
            self.dice_value_occurrence_list[self.dice_value - 1] += 1
        # print('Roll Dice Set ', self.dice_value_occurrence_list)
        return self.dice_value_occurrence_list

    def scoring_dices(self):
        self.scoring_dice = []
        for dice_index, dice_value in enumerate(self.dice_value_occurrence_list):
            if (dice_value >= params.THRESHOLD_BONUS) or (dice_index + 1 in params.LIST_SCORING_DICE_VALUE and dice_value > 0) :
                self.scoring_dice += [(dice_value, dice_index + 1)]

        return self.scoring_dice

    def nbr_scoring_dices(self):
        self.nbr_scoring_dice = 0
        for scoring_value, scoring_multiplier in zip(params.LIST_SCORING_DICE_VALUE, params.LIST_SCORING_MULTIPLIER):
            if self.dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier > 0:
                self.nbr_scoring_dice += 1
        for n, dice_value_occurrence in enumerate(self.dice_value_occurrence_list):
            nb_of_bonus = dice_value_occurrence // params.THRESHOLD_BONUS
            self.nbr_scoring_dice = self.nbr_scoring_dice + nb_of_bonus
        return self.nbr_scoring_dice