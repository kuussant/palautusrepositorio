import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_tarkista_pelaaja_haku(self):
        self.assertEqual(self.stats.search("Semenko"), self.stats._players[0])

        self.assertEqual(self.stats.search("Semenka"), None)

    def test_tarkista_tiimin_haku(self):
        searched_team = self.stats.team("EDM")

        self.assertEqual(searched_team[0], self.stats._players[0])
        self.assertEqual(searched_team[1], self.stats._players[2])
        self.assertEqual(searched_team[2], self.stats._players[4])

    def test_tarkista_sijoitus(self):
        top_2 = self.stats.top(2)

        self.assertEqual(top_2[0], self.stats._players[4])
        self.assertEqual(top_2[1], self.stats._players[1])

        top_2_by_points = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(top_2_by_points[0], self.stats._players[4])
        self.assertEqual(top_2_by_points[1], self.stats._players[1])

        top_2_by_goals = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(top_2_by_goals[0], self.stats._players[1])
        self.assertEqual(top_2_by_goals[1], self.stats._players[3])

        top_2_by_assists = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(top_2_by_assists[0], self.stats._players[4])
        self.assertEqual(top_2_by_assists[1], self.stats._players[3])

        top_2_by_any_num = self.stats.top(2, 5)
        self.assertEqual(top_2_by_any_num[0], self.stats._players[4])
        self.assertEqual(top_2_by_any_num[1], self.stats._players[1])