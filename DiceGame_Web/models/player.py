class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lost_score = 0
        self.nb_of_roll = 0
        self.nb_of_turn = 0
        self.nb_of_scoring_turn = 0
        self.nb_of_non_scoring_turn = 0
        self.nb_of_full_roll = 0
        self.is_winning = False

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
