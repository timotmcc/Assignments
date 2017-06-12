import sys
class Cybertronian:
	def __init__(self, args):
		self.name = args[0]
		self.faction = args[1]
		self.strength = int( args[2] )
		self.intelligence = int( args[3] )
		self.speed = int( args[4] )
		self.endurance = int( args[5] )
		self.rank = int( args[6] )
		self.courage = int( args[7] )
		self.firepower = int( args[8] )
		self.skill = int( args[9] )

		if self.faction not in ["A","D"]:
			sys.exit( "Bot {0} has invalid faction. Must be one of [A,D]. Exiting...".format( self.name ) )
		if not 1 <= self.strength <= 10:
			sys.exit( "Bot {0} Strength must be between 1 and 10. Exiting...".format( self.name ) )
		if not 1 <= self.intelligence <= 10:
			sys.exit( "Bot {0} Intelligence must be between 1 and 10. Exiting...".format( self.name ) )
		if not 1 <= self.speed <= 10:
			sys.exit( "Bot {0} Speed must be between 1 and 10. Exiting...".format( self.name ) )
		if not 1 <= self.endurance <= 10:
			sys.exit( "Bot {0} Endurance must be between 1 and 10. Exiting...".format( self.name ) )
		if not 1 <= self.rank <= 10:
			sys.exit( "Bot {0} Rank must be between 1 and 10. Exiting...".format( self.name ) )
		if not 1 <= self.courage <= 10:
			sys.exit( "Bot {0} Courage must be between 1 and 10. Exiting...".format( self.name ) )
		if not 1 <= self.firepower <= 10:
			sys.exit( "Bot {0} Firepower must be between 1 and 10. Exiting...".format( self.name ) )
		if not 1 <= self.skill <= 10:
			sys.exit( "Bot {0} Skill must be between 1 and 10. Exiting...".format( self.name ) )

	def getOverallRating( self ):
		return self.strength + \
			   self.intelligence + \
			   self.speed + \
			   self.endurance + \
			   self.courage + \
			   self.firepower \
			   
	def hasSpecialName( self ):
		return self.name.lower() in ["optimus prime", "predaking"]
		
	def __str__(self):
		return "Name: {0}, Faction: {1}, Rank: {2}, Overall Rating: {3}" \
			.format( self.name, self.faction, self.rank, self.getOverallRating() )