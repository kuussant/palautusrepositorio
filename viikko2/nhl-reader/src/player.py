class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.team = dict["team"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]
        self.nationality = dict["nationality"]

    def __str__(self):
        return ("{:<20}".format(self.name) 
                + "{:<5}".format(self.team) 
                + "{:<3}".format(str(self.goals)) 
                + "{:<2}".format("+") + "{:<3}".format(str(self.assists)) 
                + "{:<2}".format("=") + "{:<2}".format(self.goals+self.assists))
