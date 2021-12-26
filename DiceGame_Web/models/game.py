class Game:

    def __init__(self):
        self.final_score = 0
        self.final_ranking = 0
        self.total_roll_dice = 0
    
    def get_final_score(self) -> str:
        return self.final_score
    
    def set_final_score(self, value):
        self.final_score = value
    
    def get_final_ranking(self) -> list:
        return self.final_ranking

    def set_final_ranking(self, value):
        self.final_ranking = value

    def get_total_roll_dice(self) -> str:
        return self.total_roll_dice
    
    def set_total_roll_dice(self, value):
        self.total_roll_dice = value

    