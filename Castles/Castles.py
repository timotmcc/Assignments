def findNumCastles( input ):
	print input
	if len( input ) == 0:
		return 0
	prevValue = input[0]
	if not isinstance( prevValue, int ):
		handleTypeError( prevValue )
	prevTrend = 0
	numCastles = 1
	for land in input[1:]:
		if not isinstance( land, int ):
			handleTypeError( land )
		print land
		if land > prevValue:
			if prevTrend < 0:
				numCastles += 1
			prevTrend = 1
			prevValue = land
		elif land < prevValue:
			if prevTrend > 0:
				numCastles += 1
			prevTrend = -1
			prevValue = land
	# +1 if the last element is not part of the same peak/valley as the first element
	if prevTrend != 0:
		numCastles += 1
	return numCastles
	
def handleTypeError( value ):
	raise TypeError("{0} is not an int".format( value ) )