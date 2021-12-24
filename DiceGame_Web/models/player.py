class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.bonus_count = 0
        self.lost_count = 0
        self.roll_count = 0
        self._full_roll_count = 0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def score(self) -> str:
        return self.score

    @name.setter
    def score(self, value):
        self.score = value

    @property
    def bonus_count(self) -> int:
        return self._score

    @bonus_count.setter
    def bonus_count(self, value):
        self._bonus_count = value

    @property
    def lost_points(self) -> int:
        return self._lost_count

    @lost_points.setter
    def lost_points(self, value):
        self._lost_points = value

    @property
    def roll_count(self) -> int:
        return self._roll_count

    @roll_count.setter
    def roll_count(self, value):
        self._roll_count = value

    @property
    def full_roll_count(self) -> int:
        return self._full_roll_count

    @full_roll_count.setter
    def full_roll_count(self, value):
        self._full_roll_count = value

