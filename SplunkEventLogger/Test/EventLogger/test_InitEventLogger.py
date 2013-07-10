#@author: Deniz Ozkaynak - Created: 03/06/2013 - Last Updated: 03/06/2013
# Tests the InitEventLogger method in SplunkEventLogger.py

import os
import sys
import unittest
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir)
import SplunkEventLogger

'''
>>> InitEventLogger Testing Variables
'''
testJob = ['GetAetnaAR.bat', 'Aetna', 'GetAetnaAR.bat', 'PlanAETNA02.rpa01.com', 'EST', '12:30', '/everyweek:m,t,w,th,f,s,su', 'D:\\NaviNet\\PlanServices\\Aetna\\Scripts\GetAetnaAR.bat', '', '', '', 'VisualCron']
testHost = 'dvifsplunk01'
testStartTime = '2013-03-06T16:52:27.00Z'
testEndTime = '2013-03-06T17:52:27.00Z'
testExpectedFormatp = True

'''
>>> Test InitEventLogger Class
'''
class testInitEventLogger(unittest.TestCase):

	# Setup the testing environment before all tests run
	def setUp(self):
		self.test_eventLogger = SplunkEventLogger
		pass    # Verify environment is torn down properly
		
	# Cleanup the testing environment when the testing has finished
	def tearDown(self):
		self.test_eventLogger = None		
		pass    # Verify environment is torn down properly
		
	# Test Case 0: Compare output against an integer
	def test_initEventLogger_ExpNotEqual_int(self):
		# Get the actual output from InitEventLogger method
		logEvents_ActOut0 = self.test_eventLogger.InitEventLogger(testJob, testHost, testStartTime, testEndTime, testExpectedFormatp)
		self.maxDiff = None # This will print entire string if failure occurs
		self.assertNotEqual(logEvents_ActOut0, 19)

	# Test Case 1: Compare output against a boolean
	def test_initEventLogger_ExpNotEqual_bool(self):
		# Get the actual output from InitEventLogger method
		logEvents_ActOut0 = self.test_eventLogger.InitEventLogger(testJob, testHost, testStartTime, testEndTime, testExpectedFormatp)
		self.maxDiff = None # This will print entire string if failure occurs
		self.assertNotEqual(logEvents_ActOut0, False)
		
	# Test Case 2: Compare output against a string
	def test_initEventLogger_ExpNotEqual_str(self):
		# Get the actual output from InitEventLogger method
		logEvents_ActOut0 = self.test_eventLogger.InitEventLogger(testJob, testHost, testStartTime, testEndTime, testExpectedFormatp)
		self.maxDiff = None # This will print entire string if failure occurs
		self.assertNotEqual(logEvents_ActOut0, "foo")
		
	# Test Case 3: Compare output against an array
	def test_initEventLogger_ExpNotEqual_array(self):
		# Get the actual output from InitEventLogger method
		logEvents_ActOut0 = self.test_eventLogger.InitEventLogger(testJob, testHost, testStartTime, testEndTime, testExpectedFormatp)
		self.maxDiff = None # This will print entire string if failure occurs
		self.assertNotEqual(logEvents_ActOut0, ["bar", 0, True, None])
		
	# Test Case 4: Compare output against None keyword
	def test_initEventLogger_ExpEqual(self):
		# Get the actual output from InitEventLogger method
		logEvents_ActOut0 = self.test_eventLogger.InitEventLogger(testJob, testHost, testStartTime, testEndTime, testExpectedFormatp)
		self.maxDiff = None # This will print entire string if failure occurs
		self.assertEqual(logEvents_ActOut0, None)