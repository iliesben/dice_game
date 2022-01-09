from operator import attrgetter


class Stats:
    def __init__(self):
        self.max_score = 0
        self.longest_turn = 0
        self.max_turn_loss = 0  # max score turn
        self.mean_scoring_turn = 0
        self.mean_non_scoring_turn = 0
        self.all_score = 0
        self.nb_scoring = 0
        self.nb_non_scoring = 0
        self.all_non_score = 0

    def best_player_score(self, player):
        # best_player = list_player.sort(key=attrgetter('score'), reverse=True)
        return "\nMax turn scoring : " + str(player.name) + " with " + str(self.max_score)

    def best_longest_turn(self, player):
        return "\nMax longest turn : " + str(player.name) + " with " + str(self.longest_turn)

    def best_turn_loss(self, player):
        # lost = list_player.sort(key=attrgetter('non_potential_score'), reverse=True)
        return "\nMax turn loss : " + str(player.name) + " with " + str(self.max_turn_loss)

    # def mean_no_scoring_turn(self):
    #     return " Mean scoring turn :" + str(self.all_score / self.nb_scoring) + "(" + str(self.nb_scoring) + " turns)"

    # def mean_scoring_turn(self):
    #     return " Mean non scoring turn :" + \
    #            str(self.all_non_score / self.nb_non_scoring) + "(" + str(self.nb_non_scoring) + " turns)"
