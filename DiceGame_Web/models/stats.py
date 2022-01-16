from operator import attrgetter

class Stats:
    def __init__(self):
        self.max_score = 0
        self.longest_turn = 0
        self.max_turn_loss = 0  # max score turn
        self.mean_scoring = 0
        self.mean_non_scoring = 0
        self.all_score = 0
        self.nb_scoring = 0
        self.nb_non_scoring = 0
        self.all_non_score = 0

    def best_player_score(self, player):
        self.max_score = player.best_scoring if player.best_scoring > self.max_score else self.max_score
        return "\nMax turn scoring : " + str(self.max_score)

    def best_longest_turn(self, longest_turn):
        return "\nMax longest turn : " + str(longest_turn)

    def best_turn_loss(self, player):
        self.max_turn_loss = player.max_non_potential_score if player.max_non_potential_score > self.max_turn_loss else self.max_turn_loss
        return "\nMax turn loss : " + str(self.max_turn_loss)

    def mean_non_scoring_turn(self, player):
        self.nb_non_scoring += player.nb_of_non_scoring_turn
        self.all_non_score += player.non_potential_score
        if self.nb_non_scoring > 0:
            return "\nMean no scoring turn :" + str(self.all_non_score / self.nb_non_scoring) + "(" + str(self.nb_non_scoring) + " turns)"

    def mean_scoring_turn(self, player):
        self.all_score += player.potential_score
        print('All score : ', self.all_score)
        self.nb_scoring += player.nb_of_scoring_turn + player.nb_of_full_roll
        print('Nb of scoring : ', self.nb_scoring)
        return "\nMean scoring turn :" + str(self.all_score / self.nb_scoring) + "(" + str(self.nb_scoring) + " turns)"
