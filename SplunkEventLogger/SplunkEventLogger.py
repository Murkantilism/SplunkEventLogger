#@author: Deniz Ozkaynak - Created: 03/01/2013 - Last Updated: 03/05/2013
# This script takes a list of Unstarted Jobs and logs them as Windows
# events, to be picked up & index in Splunk.

import servicemanager
import FailedJobsLogger

PRIORITY_INFO = "<134>"
PRIORITY_WARN = "<132>"
VERSION = "1"
APPLICATION_NAME = "getUnstartedJobs.py"
MESSAGE_ID_INFO = "UnstartedJob"
MESSAGE_ID_WARN = "UnknownJobListFormat"
STRUCTURED_DATA_ID = "NaviNet@55555"
EVENT_CLASS = "JobOutput"
EVENT_SEVERITY = "Information"
EVENT_HELP = "http://wiki.navimedix.com/display/techops/Syslog+Events+From+getUnstartedJobs"

# Traceback Note: This "ParseFailedJobsLoggerOutput" method is 
# called from FailedJobsLogger.py's "findUnstartedJobs" method.

# Purpose: Create a list of strings containing the important information of
# unstarted jobs. The important info is:
# TradingPartner, JobNameInSplunk, JobNameInWiki, ServerName, 
# Timezone, TimeRun, WeeklySchedule
def InitEventLogger(job, host, TimeRangeStart, TimeRangeEnd, expectedFormatp):
	ImportantData = [] # Initialize the arraygitp
	
	# Append generic NaviNet Syslog information
	ImportantData.append('['                 + STRUCTURED_DATA_ID                 + " ")
	ImportantData.append('EventClass="'       + EVENT_CLASS                        + '" ')
	ImportantData.append('EventSeverity="'    + EVENT_SEVERITY                     + '" ')
	ImportantData.append('EventHelp="'        + EVENT_HELP                         + '" ')
	ImportantData.append('TimeRangeStart="'   + TimeRangeStart                     + '" ')
	ImportantData.append('TimeRangeEnd="'     + TimeRangeEnd                       + '" ')
	ImportantData.append('UnstartedJobName="' + job[FailedJobsLogger.JOB_NAME_COL] + '" ')
	ImportantData.append('UnstartedJobHost="' + job[FailedJobsLogger.SERVER_COL]   + '" ')
	
	# Append the important data (defined above) specific to unstarted job
	ImportantData.append('TradingPartner="'  + job[FailedJobsLogger.TRADING_PARTNER_COL]    + '" ')
	ImportantData.append('JobNameInSplunk="' + job[FailedJobsLogger.JOB_NAME_IN_SPLUNK_COL] + '" ')
	ImportantData.append('JobNameInWiki="'   + job[FailedJobsLogger.JOB_NAME_COL]           + '" ')
	ImportantData.append('Server="'          + job[FailedJobsLogger.SERVER_COL]             + '" ')
	ImportantData.append('Timezone="'        + job[FailedJobsLogger.TIMEZONE_COL]           + '" ')
	ImportantData.append('TimeRun="'         + job[FailedJobsLogger.TIME_RUN_COL]           + '" ')
	ImportantData.append('Schedule="'        + job[FailedJobsLogger.WEEKLY_SCHEDULE_COL]    + '" ')

	# Append queried server name
	ImportantData.append('QueriedServer="' + host + '"]')
	
	# If it is in the expected format, create an information event
	if (expectedFormatp):
		ReportInfoEvent(ImportantData)
	# If it is not in the expected format, create a warning event
	else:
		ReportWarningEvent(ImportantData)

def getTimeStamp():
	import time
	# Get the current UTC time at the moment this runs
	RawUTCtime = time.gmtime(time.time())
	# Convert to NaviNet Syslog format
	TimeStamp = time.strftime("%Y-%m-%dT%H:%M:%S:00Z", RawUTCtime)
	return str(TimeStamp)

# Get the hostname of this local machine
def getHostName():
	import socket
	return socket.gethostname()

# Get the process ID of this process	
def getProcID():
	import os
	return str(os.getpid())
	
# Purpose: Given a list of strings, log a Windows Error Event.
def ReportInfoEvent(ImportantData):
	# Convert ImportantData array to a string (without extraneous quotes)
	ImportantData = ''.join(ImportantData)
	# Create the Windows Event with additional Syslog info
	servicemanager.LogInfoMsg(PRIORITY_INFO     + 
							   VERSION          + " " + 
							   getTimeStamp()   + " " + 
							   getHostName()    + " " + 
							   APPLICATION_NAME + " " + 
							   getProcID()      + " " + 
							   MESSAGE_ID_INFO  + " " +
							   ImportantData)
							   
# Purpose: Given a list of strings, log a Windows Error Event.
def ReportWarningEvent(ImportantData):
	# Convert ImportantData array to a string (without extraneous quotes)
	ImportantData = ''.join(ImportantData)
	# Set the custom source name
	servicemanager.SetEventSourceName("getUnstartedJobs.py", True)	
	# Create the Windows Event with additional Syslog info
	servicemanager.LogWarningMsg(PRIORITY_WARN    + 
							     VERSION          + " " + 
							     getTimeStamp()   + " " + 
							     getHostName()    + " " + 
							     APPLICATION_NAME + " " + 
							     getProcID()      + " " + 
							     MESSAGE_ID_WARN  + " " +
							     ImportantData)