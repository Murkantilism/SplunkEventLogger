#@author: Deniz Ozkaynak - Created: 03/06/2013 - Last Updated: 03/06/2013
# Unit testing program for SplunkEventLogger.py
# *MAIN TEST FILE* - Creates test suites, runs all tests

import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir)
import unittest  # Import unittest framework
import test_InitEventLogger, test_ReportInfoEvent, test_ReportWarningEvent

'''
>>> Web Scraper Main Test Module
'''
# Create the testing suite
def eventLogging():  # Test the job event logging methods
	# Modules to load TestCases from to put into a TestSuite instance
	mySuite = [test_InitEventLogger, test_ReportInfoEvent, test_ReportWarningEvent]
	return unittest.TestSuite(map(unittest.TestLoader().loadTestsFromModule, mySuite))

# Create all_tests variable
all_tests = unittest.TestSuite()

# Add test suites
all_tests.addTest(eventLogging())

#Run all the test suites togehter
unittest.TextTestRunner(descriptions=2, verbosity=2).run(all_tests)