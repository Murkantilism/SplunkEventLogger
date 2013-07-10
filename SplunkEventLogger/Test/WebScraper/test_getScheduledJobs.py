# @author: Deniz Ozkaynak - Created: 01/16/2013 - Last Updated: 01/18/2013
# Tests the getScheduledJobs method
import os
import sys
import unittest
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir)
import WebScraper as webscraper

'''
>>> getAllScheduledJobs Testing Variables
'''
# Test files of HTML code
testHTML0 = open('testHTML0.html', 'r').read()
testHTML_broken = open('testHTML1.html', 'r').read()
testHTML_blank = open('testHTML2.html', 'r').read()
testHTML_nonHTML = open('testHTML3.txt', 'r').read()

# Expected output of getAllScheduledJobs
getJobs_ExpOut0 = [['Trading Partner', 'Job Name', 'Server', 'Timezone', 'Time Run', 'Weekly Schedule', 'Path', 'Critical', 'Job Logging?', 'Able to Run During Business Hours?', 'POC', 'Scheduler'], ['Virginia Premier', 'SetVirginiaPremierOnline.bat', 'PRWBVP01.RPA01.COM', 'GMT', '10:00', '/every:m', 'D:\\NaviNet\\TradingPartner\\VirginiaPremier\\Scripts\\SetVirginiaPremierOnline.bat', '', '', '', '', 'AT']]

# Expected output of running getAllScheduledJobs with a blank HTML file,
# a broken HTML file, a non-HTML file, an integer, a boolean, the 
# "None" keyword, & an array of literals.
getJobs_ExpOut1 = "[]"

'''
>>> Test getScheduledJobs Class
'''
class getScheduledJobsTestCase(unittest.TestCase):

	# Setup the testing environment before all tests run
	def setUp(self):
		self.test_scraper = webscraper
		pass    # Verify environment is torn down properly
		
	# Cleanup the testing environment when the testing has finished
	def tearDown(self):
		self.test_scraper = None		
		pass    # Verify environment is torn down properly
	
	# Test Case 0: Test with a normal HTML file - expect correct output
	def test_norm_getAllScheduledJobs_ExpOK(self):
		# Get the actual output from the Web Scraper
		getJobs_ActOut0 = self.test_scraper.getAllScheduledJobs(testHTML0)

		self.maxDiff = None # This will print entire string if failure occurs
		
		# Compare Actual Output with Expected Output
		self.assertEqual(getJobs_ActOut0, getJobs_ExpOut0)
	
	# Test Case 1: Test with a normal HTML file - expect failure when correct actual 
	# output is compared to incorrect expected output (empty list)
	def test_norm_getAllScheduledJobs_ExpFAIL_empty(self):
		# Get the actual output from the Web Scraper
		getJobs_ActOut1 = self.test_scraper.getAllScheduledJobs(testHTML0)		
		self.maxDiff = None
		
		# Compare Actual Output with Expected Error
		with self.assertRaises(AssertionError):
			self.assertMultiLineEqual(str(getJobs_ActOut1), "")
		
	# Test Case 2: Test with a normal HTML file - expect failure when correct actual 
	# output is compared to incorrect expected output (incomplete list of lists)
	def test_norm_getAllScheduledJobs_ExpFAIL_incompleteListOfLists(self):
		getJobs_ActOut2 = self.test_scraper.getAllScheduledJobs(testHTML0)
		self.maxDiff = None
		
		with self.assertRaises(AssertionError):
			self.assertMultiLineEqual(str(getJobs_ActOut2), 
									  "[['1199', 'Process1199SEIUExportUtilizationReports.bat', 'PRWBSEIU01.RPA01.COM', 'GMT']]")
									  
	# Test Case 3: Test with a normal HTML file - expect failure (incomplete 'singular' list)
	def test_norm_getAllScheduledJobs_ExpFAIL_incompleteList(self):
		getJobs_ActOut3 = self.test_scraper.getAllScheduledJobs(testHTML0)		
		self.maxDiff = None
		
		with self.assertRaises(AssertionError):
			self.assertMultiLineEqual(str(getJobs_ActOut3), 
									  "['1199', 'Process1199SEIUExportUtilizationReports.bat', 'PRWBSEIU01.RPA01.COM', 'GMT']")
	
	# Test Case 4: Test with a normal HTML file - expect failure (complete 'singular' list)
	def test_norm_getAllScheduledJobs_ExpFAIL_completeList(self):
		getJobs_ActOut4 = self.test_scraper.getAllScheduledJobs(testHTML0)		
		self.maxDiff = None
		
		with self.assertRaises(AssertionError):
			self.assertMultiLineEqual(str(getJobs_ActOut4), 
									  "['1199', 'Process1199SEIUExportUtilizationReports.bat', 'PRWBSEIU01.RPA01.COM', 'GMT', '17:00', '/every:5', 'D:\\\\NaviMedix\\\\NaviNet\\\\TradingPartner\\\\1199Seiu\\\\Scripts\\\\Process1199SEIUExportUtilizationReports.bat', '', '', '', 'AT ']")	
	
	# Test Case 5: Test with a BROKEN HTML file - expect failure
	def test_broken_getAllScheduledJobs_ExpFAIL(self):
		# Get the broken HTML output
		getJobs_blankOut = self.test_scraper.getAllScheduledJobs(testHTML_broken)
		# Compare against expected output
		self.assertMultiLineEqual(str(getJobs_blankOut), getJobs_ExpOut1)
			
	# Test Case 6: Test with a BLANK HTML file - expect failure
	def test_blank_getAllScheduledJobs_ExpOK(self):
		# Get the blank HTML output
		getJobs_blankOut = self.test_scraper.getAllScheduledJobs(testHTML_blank)
		# Compare against expected output
		self.assertMultiLineEqual(str(getJobs_blankOut), getJobs_ExpOut1)			
		
	# Test Case 7: Test with a NON-HTML file - expect failure
	def test_nonHTML_getAllScheduledJobs_ExpOK(self):
		# Get the non-HTML output
		getJobs_NoneOut = self.test_scraper.getAllScheduledJobs(testHTML_nonHTML)
		# Compare against expected output
		self.assertMultiLineEqual(str(getJobs_NoneOut), getJobs_ExpOut1)
			
	# Test Case 7: Test with an int - expect failure
	def test_getAllScheduledJobs_ExpOK_int(self):
		# Get the integer output
		getJobs_NoneOut = self.test_scraper.getAllScheduledJobs(19)
		# Compare against expected output
		self.assertMultiLineEqual(str(getJobs_NoneOut), getJobs_ExpOut1)	

	# Test Case 8: Test with a bool - expect failure
	def test_getAllScheduledJobs_ExpOK_bool(self):
		# Get the boolean output
		getJobs_NoneOut = self.test_scraper.getAllScheduledJobs(False)
		# Compare against expected output
		self.assertMultiLineEqual(str(getJobs_NoneOut), getJobs_ExpOut1)	
			
	# Test Case 9: Test with None - expect failure
	def test_getAllScheduledJobs_ExpOK_None(self):
		# Get the None output
		getJobs_NoneOut = self.test_scraper.getAllScheduledJobs(None)
		# Compare against expected output
		self.assertMultiLineEqual(str(getJobs_NoneOut), getJobs_ExpOut1)	

	# Test Case 7: Test with an array - expect failure
	def test_getAllScheduledJobs_ExpOK_array(self):
		# Get the array output
		getJobs_NoneOut = self.test_scraper.getAllScheduledJobs([0, 1, "0", None])
		# Compare against expected output
		self.assertMultiLineEqual(str(getJobs_NoneOut), getJobs_ExpOut1)
		
if __name__=='__main__':
   unittest.main()