from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, preader):
        reader = preader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, filter_by = SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin

        def sort_by(player):
            match filter_by:
                case SortBy.POINTS:
                    return player.points
                case SortBy.GOALS:
                    return player.goals
                case SortBy.ASSISTS:
                    return player.assists
                case _:
                    return player.points
        
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result