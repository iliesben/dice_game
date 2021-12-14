# Target total score to win by default
DEFAULT_TARGET_SCORE = 2000

# Number of dices by default in the set
DEFAULT_DICES_NB = 5
# Number of side of the dices used in the game
NB_DICE_SIDE = 6
# List of dice value scoring
LIST_SCORING_DICE_VALUE = [1, 5]
# List of associated score for scoring dice values
LIST_SCORING_MULTIPLIER = [100, 50]
# Trigger for multiple bonus
TRIGGER_OCCURRENCE_FOR_BONUS = 3
# Special bonus multiplier for multiple ace bonus
BONUS_VALUE_FOR_ACE_BONUS = 1000
# Standard multiplier for multiple dices value bonus
BONUS_VALUE_FOR_NORMAL_BONUS = 100
# Threshold of the triggering for bonus in term of occurrence of the same slide value
THRESHOLD_BONUS = 3
#Maximum roll for playing
GAME_MAX_ROLL = 5


# ----------------------------------------------------------------------------------------------------------------------
import operator
import random


# return a list of dices value occurrence for a roll of nb_dice_to_roll dices
def roll_dice_set(nb_dice_to_roll):
    dice_value_occurrence_list = [0] * NB_DICE_SIDE
    for n in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)

        dice_value_occurrence_list[dice_value - 1] += 1
    DICE_LIST = dice_value_occurrence_list
    return dice_value_occurrence_list


# return a bonus score and the new dice value occurrence without the bonus elements
def analyse_bonus_score(dice_value_occurrence_list):
    score = 0
    for side_value_index, dice_value_occurrence in enumerate(dice_value_occurrence_list):
        nb_of_bonus = dice_value_occurrence // THRESHOLD_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0:
                bonus_multiplier = BONUS_VALUE_FOR_ACE_BONUS
            else:
                bonus_multiplier = BONUS_VALUE_FOR_NORMAL_BONUS
            score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)
            dice_value_occurrence_list[side_value_index] %= THRESHOLD_BONUS
    return score, dice_value_occurrence_list


# return a standard score and dice value occurence
def analyse_standard_score(dice_value_occurrence_list):
    score = 0
    for scoring_value, scoring_multiplier in zip(LIST_SCORING_DICE_VALUE, LIST_SCORING_MULTIPLIER):
        score += dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
        dice_value_occurrence_list[scoring_value - 1] = 0
    return score, dice_value_occurrence_list


# returns the global score of the dice set and dice value occurence
def analyse_score(dice_value_occurrence_list):
    bonus_score, dice_value_occurrence_list = analyse_bonus_score(dice_value_occurrence_list)
    standard_score, dice_value_occurrence_list = analyse_standard_score(dice_value_occurrence_list)

    return bonus_score + standard_score, dice_value_occurrence_list


# returns the list of players
def set_player():
    players = int(input("Enter number of players:""\n", ))
    player_list = []
    for n in range(players):
        name = input("Enter your name:""\n", )
        player_list.append(name)
    return player_list


def nbr_scoring_dice(dice_value_list):
    nbr_scoring_dice = 0

    for scoring_value, scoring_multiplier in zip(LIST_SCORING_DICE_VALUE, LIST_SCORING_MULTIPLIER):
        if dice_value_list[scoring_value - 1] * scoring_multiplier > 0:
            nbr_scoring_dice += 1
    for side_value_index, dice_value_occurrence in enumerate(dice_value_list):
        nb_of_bonus = dice_value_occurrence // THRESHOLD_BONUS
        nbr_scoring_dice = nbr_scoring_dice + nb_of_bonus
    return nbr_scoring_dice

def launch_dice(name):
    roll = 1
    potential_score = 0
    value = 0
    dice_remaining = GAME_MAX_ROLL
    nbr_scoring = 0
    while True:
        while (dice_remaining>0):
            response = input("\n" + name + " tap [y] or [yes] for roll dice! ").lower()
            if response in ['y', 'yes']:
                dice_value_occurrence_list = roll_dice_set(DEFAULT_DICES_NB)
                nbr_scoring = nbr_scoring_dice(dice_value_occurrence_list)
                value = analyse_score(dice_value_occurrence_list)

                potential_score = potential_score + value[0]
                print(
                    "roll#" + str(roll) + " : " + str(nbr_scoring) + " scoring dices scoring " + str(value[0]) + ", potential total turn score " + str(potential_score) + ", remaining dice to roll : " + str(
                        dice_remaining))
                roll = roll + 1

            else:
                print("You win this turn, your score " + str(potential_score) + " pts")
                return value, potential_score
            dice_remaining = dice_remaining - nbr_scoring
            if dice_remaining<1:
                return value, potential_score
            if nbr_scoring == 0:
                print(
                    "Roll#" + str(roll) + " : " + str(nbr_scoring) + " scoring dices scoring " + str(
                        value[0]) + ", potential total turn score " + str(
                        potential_score) + ", remaining dice to roll : " + str(
                        dice_remaining))
                print("You lose this turn and a potential to score "+str(potential_score)+" pts")
                return value, potential_score

        return value, potential_score

def ranking_final_score(score_dict):
    sort_score_dict = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)

    str_score = "total score : "
    for player, score in sort_score_dict:
        str_score += player + " --> " + str(score) + " , "
    return str_score


def game_start():
    list_player = set_player()
    global_score = {}
    max_score = 0
    index_turn = 1
    while max_score < DEFAULT_TARGET_SCORE:
        indexplayer = 0
        score_final_turn = 0
        score_dict = {}
        score = [0] * len(list_player)
        print("Turn #"+str(index_turn))
        for name in list_player:
             score_player = launch_dice(name)
             score[indexplayer] = score_player[0]
             score_final_turn = score_final_turn + score_player[1]
             score_dict[name] = score_final_turn
             global_score[name] = global_score[name] + score_final_turn if name in global_score else score_final_turn
             max_score = global_score[name]
             print("global_score : ", global_score)
             print("max_score : ", max_score)
             indexplayer += 1
        index_turn = index_turn+1


    print(ranking_final_score(global_score))

game_start()
