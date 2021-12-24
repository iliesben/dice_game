class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.bonus_count = 0
        self.lost_count = 0
        self.roll_count = 0
        self.full_roll_count = 0
        self.is_winning = False

    def get_name(self) -> str:
        return self.name

    def set_name(self, value):
        self.name = value

    def get_score(self) -> int:
        return self.score

    def set_score(self, value):
        self.score = value

    def get_bonus_count(self) -> int:
        return self.bonus_count

    def set_bonus_count(self, value):
        self.bonus_count = value

    def get_lost_points(self) -> int:
        return self.lost_count

    def set_lost_points(self, value):
        self.lost_count = value

    def get_roll_count(self) -> int:
        return self.roll_count

    def set_roll_count(self, value):
        self.roll_count = value

    def get_full_roll_count(self) -> int:
        return self.full_roll_count

    def set_full_roll_count(self, value):
        self.full_roll_count = value

    def is_winning(self) -> bool:
        return self.is_winning

    def is_winning(self, value):
        self.is_winning = value
