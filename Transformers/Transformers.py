import sys
from Cybertronian import Cybertronian

class DestroyAllCompetitors(Exception):
    pass

def checkNames( autobot, decepticon ):
	if autobot.hasSpecialName() and decepticon.hasSpecialName():
		print "{0} vs {1}. Destroying all competitors".format( autobot.name, decepticon.name )
		raise DestroyAllCompetitors
	elif autobot.hasSpecialName():
		return 1
	elif decepticon.hasSpecialName():
		return 2
	else:
		return 0

def checkCourageStrength( autobot, decepticon ):
	if ( autobot.courage - decepticon.courage ) >=4 and \
	   ( autobot.strength - decepticon.strength ) >=3:
		return 1
	elif ( decepticon.courage - autobot.courage ) >=4 and \
	   ( decepticon.strength - autobot.strength ) >=3:
		return 2
	else:
		return 0

def checkSkill( autobot, decepticon ):
	if ( autobot.skill - decepticon.skill ) >=3:
		return 1
	elif ( decepticon.skill - autobot.skill ) >=3:
		return 2
	else:
		return 0

def checkOverallrating( autobot, decepticon ):
	if ( autobot.getOverallRating() > decepticon.getOverallRating() ):
		return 1
	elif ( decepticon.getOverallRating() > autobot.getOverallRating() ):
		return 2
	else:
		return 0

def main():
	autobots = []
	decepticons = []
	survivingAutobots = []
	survivingDecepticons = []

	if len( sys.argv ) < 2:
		sys.exit( 'Usage: {0} <filename>'.format( sys.argv[0] ) )

	inFile = sys.argv[1]
	with open( inFile ) as f:
		lines = f.readlines()

	for line in lines:
		params = line.split( ',' )
		botData = [ asdf.strip() for asdf in line.split( ',' ) ]
		newBot = Cybertronian( botData )
		if newBot.faction == "D":
			decepticons.append( newBot )
		elif newBot.faction == "A":
			autobots.append( newBot )

	autobots.sort( key=lambda x: x.rank, reverse=True )
	decepticons.sort( key=lambda x: x.rank, reverse=True )

	autobotWins = 0
	decepticonWins = 0
	numFights = 0
	try:
		for botA, botD in zip( autobots, decepticons ):
			numFights += 1
			fightResult = checkNames( botA, botD )
			if not fightResult:
				fightResult = checkCourageStrength( botA, botD )
			if not fightResult:
				fightResult = checkSkill( botA, botD )
			if not fightResult:
				fightResult = checkOverallrating( botA, botD )

			if fightResult == 1:
				autobotWins +=1
				survivingAutobots.append( botA.name )
			elif fightResult == 2:
				decepticonWins += 1
				survivingDecepticons.append( botD.name )
			else:
				#it's a tie! don't count any win, and don't save either bot's name
				pass

		#append bots that had no matchup
		if( len( autobots ) > len( decepticons ) ):
			survivingAutobots += [bot.name for bot in autobots[len( decepticons ):]]
		elif( len( decepticons ) > len( autobots ) ):
			survivingDecepticons += [bot.name for bot in decepticons[len( autobots ):]]

		if autobotWins > decepticonWins:
			winningTeam = "Autobots"
			winnerNames = [bot.name for bot in autobots]
			losingTeam = "Decepticons"
			survivingLosers = survivingDecepticons
		elif decepticonWins > autobotWins:
			winningTeam = "Decepticons"
			winnerNames = [bot.name for bot in decepticons]
			losingTeam = "Autobots"
			survivingLosers = survivingAutobots
		else:
			winningTeam = "None"
			winnerNames = ""
			losingTeam = "Both"
			survivingLosers = survivingAutobots + survivingDecepticons

	except DestroyAllCompetitors:
		winningTeam = "None"
		winnerNames = ""
		losingTeam = "Both"
		survivingLosers = []

	print "{0} battle{1}".format( numFights, "s" if numFights!=1 else "" )
	print "Winning team ({0}): {1}".format( winningTeam, ', '.join( winnerNames ) )
	print "Survivors from the losing team ({0}): {1}".format( losingTeam, ', '.join( survivingLosers ) )

if __name__=='__main__':
	main()
