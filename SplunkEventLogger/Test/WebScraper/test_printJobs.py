# @author: Deniz Ozkaynak - Created: 01/16/2013 - Last Updated: 01/18/2013
# Tests the printJobs method

import unittest
import unittest
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir)
import WebScraper as webscraper

'''
>>> printJobs Testing Variables
'''
# Test file of HTML code
testHTML0 = open('testHTML0.html', 'r').read()

testPrintJobs0 = webscraper.getAllScheduledJobs(testHTML0)
testPrintJobs1 = "This is not a print job"

# Expected Output
printJobsExpOut = 'None'
printJobsExpOut1 = "[['1199', 'Process1199SEIUExportUtilizationReports.bat', 'PRWBSEIU01.RPA01.COM', 'GMT', '17:00', '/every:5', 'D:\NaviMedix\NaviNet\TradingPartner\1199Seiu\Scripts\Process1199SEIUExportUtilizationReports.bat', '', '', '', 'AT ']]"


'''
>>> Test printJobs Class
'''
class printJobsTestCase(unittest.TestCase):

	# Setup the testing environment before all tests run
	def setUp(self):
		self.test_scraper = webscraper
		pass    # Verify environment is torn down properly
		
	# Cleanup the testing environment when the testing has finished
	def tearDown(self):
		self.test_scraper = None		
		pass    # Verify environment is torn down properly
	
	# Test Case 0: incorrect type of input - int
	def test_printJobs_ExpFAIL_int(self):
		# Compare Actual Output with Expected Error
		with self.assertRaises(TypeError):
			self.test_scraper.printJobs(17)
			
	# Test Case 1: incorrect type of input - bool
	def test_printJobs_ExpFAIL_bool(self):
		with self.assertRaises(TypeError):
			self.test_scraper.printJobs(False)
			
	# Test Case 2: incorrect type of input - None
	def test_printJobs_ExpFAIL_None(self):
		with self.assertRaises(TypeError):
			self.test_scraper.printJobs(None)
			
	# Test Case 3: incorrect type of input - array
	def test_printJobs_ExpFAIL_array(self):
		with self.assertRaises(TypeError):
			self.test_scraper.printJobs([6, 0, "3", None, True])
			
if __name__=='__main__':
   unittest.main()