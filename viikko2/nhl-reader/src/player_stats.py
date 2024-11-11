class PlayerStats:
    def __init__(self, stats):
        self.players = stats.get_players()

    def top_scorers_by_nationality(self, nationality):

        def sort_by_score(p):
            return p.goals + p.assists
        
        sorted_players = sorted(self.players, reverse=True, key=sort_by_score)

        out = []

        print("Players from " + f"{nationality}" + ":\n")

        for player in sorted_players:
            if player.nationality == nationality:
                out.append(player)

        return out