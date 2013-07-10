#@author: Deniz Ozkaynak - Created: 03/06/2013 - Last Updated: 03/06/2013
# Tests the ReportInfoEvent method in SplunkEventLogger.py

import os
import sys
import unittest
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir)
import SplunkEventLogger

'''
>>> ReportInfoEvent Testing Variables
'''
testImportantData = ['[NaviNet@55555 ', 'EventClass="JobOutput" ', 'EventSeverity="Information" ', 'EventHelp="http://wiki.navimedix.com/display/techops/Syslog+Events+From+getUnstartedJobs" ', 'TimeRangeStart="2013-03-06T17:26:59.00Z" ', 'TimeRangeEnd="2013-03-06T18:26:59.00Z" ', 'UnstartedJobName="GenerateVirginiaPremierRefAuthSubmissions.bat" ', 'UnstartedJobHost="PRWBVP01.RPA01.COM" ', 'TradingPartner="Virginia Premier" ', 'JobNameInSplunk="GenerateVirginiaPremierRefAuthSubmissions.bat" ', 'JobNameInWiki="GenerateVirginiaPremierRefAuthSubmissions.bat" ', 'Server="PRWBVP01.RPA01.COM" ', 'Timezone="GMT" ', 'TimeRun="17:50" ', 'Schedule="/everyweek:m,t,w,th,f,s" ', 'QueriedServer="dvifsplunk01"]']

'''
>>> Test ReportInfoEvent Class
'''
class testReportInfoEvent(unittest.TestCase):

	# Setup the testing environment before all tests run
	def setUp(self):
		self.test_eventLogger = SplunkEventLogger
		pass    # Verify environment is torn down properly
		
	# Cleanup the testing environment when the testing has finished
	def tearDown(self):
		self.test_eventLogger = None		
		pass    # Verify environment is torn down properly
		
	# Test Case 0: Compare output against an integer
	def test_reportInfoEvent_ExpNotEqual_int(self):
		# Get the actual output from InitEventLogger method
		reportEvents_ActOut0 = self.test_eventLogger.ReportInfoEvent(testImportantData)
		self.maxDiff = None # This will print entire string if failure occurs
		self.assertNotEqual(reportEvents_ActOut0, 19)

	# Test Case 1: Compare output against a boolean
	def test_reportInfoEvent_ExpNotEqual_bool(self):
		# Get the actual output from InitEventLogger method
		reportEvents_ActOut1 = self.test_eventLogger.ReportInfoEvent(testImportantData)
		self.maxDiff = None # This will print entire string if failure occurs
		self.assertNotEqual(reportEvents_ActOut1, False)
		
	# Test Case 2: Compare output against a string
	def test_reportInfoEvent_ExpNotEqual_str(self):
		# Get the actual output from InitEventLogger method
		reportEvents_ActOut2 = self.test_eventLogger.ReportInfoEvent(testImportantData)
		self.maxDiff = None # This will print entire string if failure occurs
		self.assertNotEqual(reportEvents_ActOut2, "foo")
		
	# Test Case 3: Compare output against an array
	def test_reportInfoEvent_ExpNotEqual_array(self):
		# Get the actual output from InitEventLogger method
		reportEvents_ActOut3 = self.test_eventLogger.ReportInfoEvent(testImportantData)
		self.maxDiff = None # This will print entire string if failure occurs
		self.assertNotEqual(reportEvents_ActOut3, ["bar", 0, True, None])
		
	# Test Case 4: Compare output against None keyword
	def test_reportInfoEvent_ExpEqual(self):
		# Get the actual output from InitEventLogger method
		reportEvents_ActOut4 = self.test_eventLogger.ReportInfoEvent(testImportantData)
		self.maxDiff = None # This will print entire string if failure occurs
		self.assertEqual(reportEvents_ActOut4, None)