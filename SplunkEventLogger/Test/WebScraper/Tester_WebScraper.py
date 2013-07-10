# @author: Deniz Ozkaynak - Created: 01/16/2013 - Last Updated: 01/18/2013
# Unit testing for WebScraper.py
# *MAIN TEST FILE* - Creates test suites, runs all tests

import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir)
import unittest       # Import unittest framework
import test_getScheduledJobs, test_printJobs
import test_removeTagsFromLine, test_removeFunkyCharsFromLine

'''
>>> Web Scraper Main Test Module
'''
# Create the testing suites
def jobs_suite():  # Test the job schedule methods
	# Modules to load TestCases from to put into a TestSuite instance
	mySuite = [test_getScheduledJobs, test_printJobs]
	return unittest.TestSuite(map(unittest.TestLoader().loadTestsFromModule, mySuite))

def remove_suite():  # Test the removal methods
	# Modules to load TestCases from to put into a TestSuite instance
	mySuite = [test_removeTagsFromLine, test_removeFunkyCharsFromLine]		
	return unittest.TestSuite(map(unittest.TestLoader().loadTestsFromModule, mySuite))
	
# Create all_tests variable
all_tests = unittest.TestSuite()

# Add test suites
all_tests.addTest(jobs_suite())
all_tests.addTest(remove_suite())

#Run all the test suites togehter
unittest.TextTestRunner(descriptions=10, verbosity=10).run(all_tests)