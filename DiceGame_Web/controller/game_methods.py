import random
import operator
import utils.constants as params
from models.player import Player
import controller.player_methods as player
import controller.score_methods as score_methods


def add_player():
    number_of_players = int(input("Enter number of players:\n", ))
    player_list = []
    for _ in range(number_of_players):
        name_player: str = input("Enter your name:\n", )
        player_list.append(Player(name_player))
    return player_list


def init_global_score(list_player):
    global_score = {}

    for name in list_player:
        global_score[name] = 0

    return global_score


def display_global_score(global_score):
    total_score = "total score : "
    global_score_sorted = sorted(global_score.items(), key=operator.itemgetter(1), reverse=True)

    for name, score in global_score_sorted:
        total_score += Player.get_name(name) + ' --> ' + str(score) + ' '

    return total_score


def launch_game():
    stats_dice_game = {"max_game_turn": 0,
                       "max_turn_scoring": 0,
                       "longest_turn": 0,
                       "max_turn_loss": 0,
                       "mean_scoring_turn": 0,
                       "max_scoring_turn": 0,
                       "mean_noscoring_turn": 0,
                       "max_noscoring_turn": 0
                       }
    stats_player_roll = {}
    stats_player_loss = {}
    stats_player_bonus = {}

    list_player = add_player()
    global_score = init_global_score(list_player)
    max_score = 0
    index_turn = 1
    while max_score < params.DEFAULT_TARGET_SCORE:
        # game turn
        indexplayer = 0
        score_dict = {}
        score = [0] * len(list_player)
        print("\n" + "Turn #" + str(index_turn))
        # player turn
        for name in list_player:
            score_final_turn = 0
            score_player = player.launch_dice(name, global_score)
            score[indexplayer] = score_player[0]
            score_final_turn = score_final_turn + score_player[1]
            score_dict[name] = score_final_turn
            global_score[name] = global_score[name] + score_final_turn if name in global_score else score_final_turn
            max_score = global_score[name]
            print('global score ', global_score[name])
            print('Stats dice game ', stats_dice_game["max_game_turn"])
            print(display_global_score(global_score))
            if global_score[name] > params.DEFAULT_TARGET_SCORE:
                score_methods.ranking_final_score(global_score, stats_dice_game["max_game_turn"])
                return print("END GAME")
            indexplayer += 1
        # end player turn
        index_turn = index_turn + 1
        stats_dice_game["max_game_turn"] = index_turn
        # end game turn
    score_methods.ranking_final_score(global_score, stats_dice_game["max_game_turn"])
    print(stats_dice_game)

