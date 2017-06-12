from Castles import findNumCastles
import unittest

class TestCastles( unittest.TestCase ):

	def test_empty( self ):
		self.assertEqual( findNumCastles( [] ), 0 )

	def test_single( self ):
		self.assertEqual( findNumCastles( [1] ), 1 )

	def test_peak( self ):
		self.assertEqual( findNumCastles( [1,2,1] ), 3 )

	def test_plateau( self ):
		self.assertEqual( findNumCastles( [2,6,6,6,3] ), 3 )

	def test_longsequences( self ):
		self.assertEqual( findNumCastles( [1,2,3,4,2,3,4,5] ), 4 )

	def test_staircase( self ):
		self.assertEqual( findNumCastles( [1,1,2,2,3,3,4,4] ), 2 )
		
	def test_duplicatesAtEnd( self ):
		self.assertEqual( findNumCastles( [1,2,2,2] ), 2 )

	def test_plains( self ):
		self.assertEqual( findNumCastles( [1,1,1,1,1] ), 1 )

	def test_badDataType( self ):
		self.assertRaises( TypeError, lambda: findNumCastles( [1,2,3.14] ) )

if __name__ == "__main__":
	unittest.main()
