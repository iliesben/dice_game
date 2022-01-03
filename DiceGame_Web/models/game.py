from models.player import Player

class Game:

    def __init__(self):
        self.number_of_players = 0
        self.player_list = []
        self.global_score = {}
        # self.final_score = 0
        # self.final_ranking = 0
        # self.total_roll_dice = 0

    def get_number_of_players(self) -> int:
        return self.number_of_players
    
    def set_number_of_players(self, value):
        self.number_of_players = value
    
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

    def add_player(self):
        self.number_of_players = int(input("Enter number of players:\n", ))
        for _ in range(self.number_of_players):
            name_player: str = input("Enter your name:\n", )
            self.player_list = Player(name_player)
        return self.player_list
    
    def init_global_score(self):

        for name in self.player_list:
            self.global_score[name] = 0
            print(self.global_score[name])

        return self.global_score