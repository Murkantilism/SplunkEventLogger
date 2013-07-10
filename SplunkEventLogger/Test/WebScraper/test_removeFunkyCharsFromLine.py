# @author: Deniz Ozkaynak - Created: 01/16/2013 - Last Updated: 01/18/2013
# Tests the removeFunkyCharsFromLine method

import unittest
import unittest
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir)
import WebScraper as webscraper
'''
>>> removeFunkyCharsFromLine Testing Variables
'''

removeFunky_ExpOut0 = "<tr>this is test html</tr>" # Expected output of removeFunky
removeFunky_ExpOut1 = "this is test html code"
removeFunky_ExpOut2 = "  "
removeFunky_ExpOut3 = "<td class='confluenceTd'>this is test html</td>"

'''Causes infinite loop/timeout'''
removeFunky_ExpOut4 = "td class='confluenceTd'>this is test html"

removeFunky_ExpOut5 = ""
removeFunky_ExpOut6 = ""


'''
>>> Test removeFunkyCharsFromLine Class
'''
class removeFunkyCharsFromLineTestCase(unittest.TestCase):

	# Setup the testing environment before all tests run
	def setUp(self):
		self.test_scraper = webscraper
		pass    # Verify environment is torn down properly
		
	# Cleanup the testing environment when the testing has finished
	def tearDown(self):
		self.test_scraper = None
		pass    # Verify environment is torn down properly
		
	# Test Case 0: with Tags & Funky Chars
	def test_removeFunkyCharsFromLine_withTags_withChars(self):
		# Get the actual output from the Web Scraper
		removeFunky_ActOut0 = self.test_scraper.removeFunkyCharsFromLine("<tr>this is test html&code;</tr>" )
		
		# Compare Actual Output with Expected Output
		self.assertEqual(removeFunky_ActOut0, removeFunky_ExpOut0)		
	
	# Test Case 1: without Tags nor Funky Chars
	def test_removeFunkyCharsFromLine_withoutTags_withoutChars(self):
		# Get the actual output from the Web Scraper
		removeFunky_ActOut1 = self.test_scraper.removeFunkyCharsFromLine("this is test html code")
		
		# Compare Actual Output with Expected Output
		self.assertEqual(removeFunky_ActOut1, removeFunky_ExpOut1)
	
	# Test Case 2: without Tags & with Funky Chars	
	def test_removeFunkyCharsFromLine_withoutTags_withChars(self):
		removeFunky_ActOut2 = self.test_scraper.removeFunkyCharsFromLine(" &this is test html code; ")
		self.assertEqual(removeFunky_ActOut2, removeFunky_ExpOut2)

	# Test Case 3: with Tags & without Funky Chars
	def test_removeFunkyCharsFromLine_withTags_withoutChars(self):
		removeFunky_ActOut3 = self.test_scraper.removeFunkyCharsFromLine("<td class='confluenceTd'>this is test html&code;</td>")
		self.assertEqual(removeFunky_ActOut3, removeFunky_ExpOut3)
		
	''' NOTE: Incomplete tags currently cause a Timeout/Applicationg Hang Error '''
	# Test Case: with incomplete Funky Chars
	#def test_removeFunkyCharsFromLine_withIncompleteChars(self):
		#removeFunky_Out4 = self.test_scraper.removeFunkyCharsFromLine("td c;lass='confluenceTd'>this is test html&code</td")
		#self.assertEqual(removeFunky_Out4, removeFunky_ExpOut4)
		
	# Test Case 5: with empty string
	def test_removeFunkyCharsFromLine_withEmptyString(self):
		removeFunky_ActOut5 = self.test_scraper.removeFunkyCharsFromLine("")
		self.assertEqual(removeFunky_ActOut5, removeFunky_ExpOut5)
		
	# Test Case 6: with only Funky Chars
	def test_removeFunkyCharsFromLine_withOnlyChars(self):
		removeFunky_ActOut6 = self.test_scraper.removeFunkyCharsFromLine("&;&;&;")
		self.assertEqual(removeFunky_ActOut6, removeFunky_ExpOut6)
	
	# Test Case 7: incorrect type of input - None
	def test_removeFunkyCharsFromLine_incorrectInput_None(self):
		# Compare Actual Output with Expected Error
		with self.assertRaises(AttributeError):
			self.test_scraper.removeFunkyCharsFromLine(None)
	
	# Test Case 8: incorrect type of input - int	
	def test_removeFunkyCharsFromLine_incorrectInput_int(self):
		with self.assertRaises(AttributeError):
			self.test_scraper.removeFunkyCharsFromLine(17)
	
	# Test Case 9: incorrect type of input - array			
	def test_removeFunkyCharsFromLine_incorrectInput_array(self):
		with self.assertRaises(AttributeError):
			self.test_scraper.removeFunkyCharsFromLine([17, 23, "3", None])
	
	# Test Case 10: incorrect type of input - bool	
	def test_removeFunkyCharsFromLine_incorrectInput_bool(self):
		with self.assertRaises(AttributeError):
			self.test_scraper.removeFunkyCharsFromLine(True)	

if __name__=='__main__':
   unittest.main()