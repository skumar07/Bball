from random import randint

class Game(object):
	def __init__(self, home, away):
		self.hometeam = home
		self.awayteam = away
		self.score = (0,0)

	def simulate_pos(self, team):
		perentage = team.stats.FGP
		random_num = randint(1,100)
		

