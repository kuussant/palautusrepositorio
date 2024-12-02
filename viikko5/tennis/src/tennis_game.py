LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self._get_equal_score_call(self.player1_score)

        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self._get_advantage_call(self.player1, self.player2, self.player1_score, self.player2_score)

        else:
            score = self._get_score_call(self.player1_score) + "-" + self._get_score_call(self.player2_score)

        return score
    
    def _get_score_call(self, score):
        call = ""

        if score == LOVE:
            call = "Love"
        elif score == FIFTEEN:
            call = "Fifteen"
        elif score == THIRTY:
            call = "Thirty"
        elif score == FORTY:
            call = "Forty"

        return call
    
    def _get_equal_score_call(self, score):
        call = ""
        if score >= FORTY:
            call = "Deuce"
        else:
            call = self._get_score_call(score) + "-All"
        return call
    
    def _get_advantage_call(self, player1, player2, player1_score, player2_score):
            score_difference = abs(player1_score - player2_score)
            call = ""
            winning_player = ""

            if player1_score > player2_score:
                winning_player = player1
            else:
                winning_player = player2

            if score_difference == 1:
                call = f"Advantage {winning_player}"
            elif score_difference >= 1:
                call = f"Win for {winning_player}"

            return call
