import operator
import utils.constants as params
from models.player import Player

class Game:

    def __init__(self):
        self.number_of_players = 0
        self.player_list = []
        self.global_score = {}
        self.max_score = 0
        self.score_final_turn = 0

        self.stats_dice_game = {
            "max_game_turn": 0,
            "max_turn_scoring": 0,
            "longest_turn": 0,
            "max_turn_loss": 0,
            "mean_scoring_turn": 0,
            "max_scoring_turn": 0,
            "mean_noscoring_turn": 0,
            "max_noscoring_turn": 0
        }


    def add_player(self):
        self.number_of_players = int(input("Enter number of players:\n", ))
        for _ in range(self.number_of_players):
            name_player: str = input("Enter your name:\n", )
            self.player_list.append(Player(name_player))
        print(type(self.player_list))
        return self.player_list


    def launch_game(self):
        list_player = self.add_player()
        # global_score = init_global_score(list_player)
        index_turn = 1
        while self.max_score <= params.DEFAULT_TARGET_SCORE:
            # game turn
            indexplayer = 0
            score_dict = {}
            score = [0] * len(list_player)
            print("\n" + "Turn #" + str(index_turn))
            # player turn
            for player in list_player:
                score_final_turn = 0
                score_of_player, potential_of_player = player.launch_dice()
                score[indexplayer] = score_of_player
                print('score_player of :', player.name, ' ', score)

                score_final_turn = score_final_turn + potential_of_player
                score_dict[player.name] = score_final_turn
                # print('Score dict', score_dict)
                
                # global_score[name] = global_score[name] + score_final_turn if name in global_score else score_final_turn
                # print('Player score before', player.score)
                # print('Score final turn ', score_final_turn)
                # # player.score += score_final_turn
                # print('player score : ', player.score)

                self.max_score += player.score
                print('Max score ', self.max_score)
                
                # print('global score ', global_score[name])
                # print('Stats dice game ', self.stats_dice_game["max_game_turn"])
                # print(self.display_global_score(global_score))
                if player.score >= params.DEFAULT_TARGET_SCORE:
                    # score_methods.ranking_final_score(global_score, self.stats_dice_game["max_game_turn"])
                    return print("END GAME")
                indexplayer += 1
            # end player turn
            # index_turn = index_turn + 1
            # self.stats_dice_game["max_game_turn"] = index_turn
            # end game turn
        # self.ranking_final_score(global_score, self.stats_dice_game["max_game_turn"])
        # print(self.stats_dice_game) 

    def ranking_final_score(score_dict, index_turn):
        sort_score_dict = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)

        classment_score = ""
        for count, (player, score) in enumerate(sort_score_dict):
            if (count == 0):
                classment_score += Player.get_name(player) + " win ! scoring " + str(score) + "\n"
            else:
                classment_score += Player.get_name(player) + " lose ! scoring " + str(score) + "\n"

        print("Game in " + str(index_turn) + " turn(s)")
        print(classment_score)

    def display_global_score(global_score):
        total_score = "total score : "
        global_score_sorted = sorted(global_score.items(), key=operator.itemgetter(1), reverse=True)

        for name, score in global_score_sorted:
            total_score += Player.get_name(name) + ' --> ' + str(score) + ' '

        return total_score


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
