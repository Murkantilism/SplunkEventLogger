# @author: Deniz Ozkaynak - Created: 01/16/2013 - Last Updated: 01/18/2013
# Tests the removeTagsFromLine method

import unittest
import unittest
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir)
import WebScraper as webscraper

'''
>>> removeTagsFromLine Testing Variables
'''
# Expected output of removeTags
removeTags_ExpOut0 = "this is test html&code;"
removeTags_ExpOut1 = "this is test html code"
removeTags_ExpOut2 = " &this is test html code; "
removeTags_ExpOut3 = "this is test html&code;"
removeTags_ExpOut4 = "td class='confluenceTd'>this is test html"
removeTags_ExpOut5 = ""
removeTags_ExpOut6 = ""


'''
>>> Test removeTagsFromLine Class
'''
class removeTagsFromLineTestCase(unittest.TestCase):

	# Setup the testing environment before all tests run
	def setUp(self):
		self.test_scraper = webscraper
		pass    # Verify environment is torn down properly
		
	# Cleanup the testing environment when the testing has finished
	def tearDown(self):
		self.test_scraper = None		
		pass    # Verify environment is torn down properly
		
	# Test Case 0: with Tags & Funky Chars
	def test_removeTagsFromLine_withTags_withChars(self):
		# Get the actual output from the Web Scraper
		removeTags_Out0 = self.test_scraper.removeTagsFromLine("<tr>this is test html&code;</tr>")
		
		# Compare Actual Output with Expected Output
		self.assertEqual(removeTags_Out0, removeTags_ExpOut0)
	
	# Test Case 1: without Tags nor Funky Chars
	def test_removeTagsFromLine_withoutTags_withoutChars(self):
		# Get the actual output from the Web Scraper
		removeTag_Out1 = self.test_scraper.removeTagsFromLine("this is test html code")
		
		# Compare Actual Output with Expected Output
		self.assertEqual(removeTag_Out1, removeTags_ExpOut1)
		
	# Test Case 2: without Tags & with Funky Chars
	def test_removeTagsFromLine_withoutTags_withChars(self):
		removeTag_Out2 = self.test_scraper.removeTagsFromLine(" &this is test html code; ")
		self.assertEqual(removeTag_Out2, removeTags_ExpOut2)
		
	# Test Case 3: with Tags & without Funky Chars
	def test_removeTagsFromLine_withTags_withoutChars(self):
		removeTag_Out3 = self.test_scraper.removeTagsFromLine("<td class='confluenceTd'>this is test html&code;</td>")
		self.assertEqual(removeTag_Out3, removeTags_ExpOut3)
		
	''' NOTE: Incomplete tags currently cause a Timeout/Applicationg Hang Error '''
	# Test Case 4: with incomplete Tags - expect timeout error
	#def test_removeTagsFromLine_withIncompleteTags(self):	
		#removeTag_Out4 = self.test_scraper.removeTagsFromLine("td class='confluenceTd'>this is test html&code;</td")
		#self.assertEqual(removeTag_Out4, removeTags_ExpOut4)
		
	# Test Case 5: with empty string
	def test_removeTagsFromLine_withEmptyString(self):
		removeTag_Out5 = self.test_scraper.removeTagsFromLine("")
		self.assertEqual(removeTag_Out5, removeTags_ExpOut5)
		
	# Test Case 6: with only tags
	def test_removeTagsFromLine_withOnlyTags(self):
		removeTag_Out6 = self.test_scraper.removeTagsFromLine("<td></td>")
		self.assertEqual(removeTag_Out6, removeTags_ExpOut6)
		
	# Test Case 7: incorrect type of input - None
	def test_removeTagsFromLine_incorrectInput_None(self):
		# Compare Actual Output with Expected Error
		with self.assertRaises(AttributeError):
			self.test_scraper.removeTagsFromLine(None)
		
	# Test Case 8: incorrect type of input - int
	def test_removeTagsFromLine_incorrectInput_int(self):
		with self.assertRaises(AttributeError):
			self.test_scraper.removeTagsFromLine(17)
			
	# Test Case 9: incorrect type of input - array
	def test_removeTagsFromLine_incorrectInput_array(self):
		with self.assertRaises(AttributeError):
			self.test_scraper.removeTagsFromLine([17, 23, "3", None])

	# Test Case 10: incorrect type of input - bool
	def test_removeTagsFromLine_incorrectInput_bool(self):
		with self.assertRaises(AttributeError):
			self.test_scraper.removeTagsFromLine(True)
			
if __name__=='__main__':
   unittest.main()