import operator

from models.stats import Stats
import utils.constants as params
from models.player import Player
from utils import utils


class Game:

    def __init__(self):
        self.number_of_players = 0
        self.player_list = []
        self.max_score = 0

    def add_player(self):
        self.number_of_players = int(input("Enter number of players:\n", ))
        for _ in range(self.number_of_players):
            name_player: str = input("Enter your name:\n", )
            self.player_list.append(Player(name_player))
        return self.player_list

    def launch_game(self):

        list_player = self.add_player()
        app_stat = Stats()
        index_turn = 1

        while self.max_score <= params.DEFAULT_TARGET_SCORE:
            # game turn
            print("\n" + "Turn #" + str(index_turn))
            # player turn
            for player in list_player:

                score_of_player, potential_of_player = player.launch_dice()
                self.max_score = player.score

                app_stat.max_score = player.best_scoring \
                    if player.best_scoring > app_stat.max_score else app_stat.max_score
                app_stat.all_score += player.score

                if player.score >= params.DEFAULT_TARGET_SCORE:
                    return print("END GAME")

                print(utils.parse_to_str(player.name) + " ton score est : " + utils.parse_to_str(player.score)
                      + " potential score est :" + utils.parse_to_str(player.potential_score)
                      + " best score est : " + utils.parse_to_str(player.best_scoring))

    # def ranking_final_score(score_dict, index_turn):
    #     sort_score_dict = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)
    #
    #     classment_score = ""
    #     for count, (player, score) in enumerate(sort_score_dict):
    #         if (count == 0):
    #             classment_score += Player.get_name(player) + " win ! scoring " + str(score) + "\n"
    #         else:
    #             classment_score += Player.get_name(player) + " lose ! scoring " + str(score) + "\n"
    #
    #     print("Game in " + str(index_turn) + " turn(s)")
    #     print(classment_score)
    #
    # def display_global_score(global_score):
    #     total_score = "total score : "
    #     global_score_sorted = sorted(global_score.items(), key=operator.itemgetter(1), reverse=True)
    #
    #     for name, score in global_score_sorted:
    #         total_score += Player.get_name(name) + ' --> ' + str(score) + ' '
    #
    #     return total_score

    # def get_number_of_players(self) -> int:
    #     return self.number_of_players

    # def set_number_of_players(self, value):
    #     self.number_of_players = value

    # def get_final_score(self) -> str:
    #     return self.final_score

    # def set_final_score(self, value):
    #     self.final_score = value

    # def get_final_ranking(self) -> list:
    #     return self.final_ranking

    # def set_final_ranking(self, value):
    #     self.final_ranking = value

    # def get_total_roll_dice(self) -> str:
    #     return self.total_roll_dice

    # def set_total_roll_dice(self, value):
    #     self.total_roll_dice = value
