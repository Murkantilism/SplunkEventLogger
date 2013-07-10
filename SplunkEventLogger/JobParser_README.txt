NOTE: Open this file in Notepad++ or another code editor, not Notepad.
@author: Deniz Ozkaynak - Created: 01/16/2013 - Last Updated: 01/22/2013

This project folder contains files for Web Scraping html code and parsing
the output to create a list of Splunk Scheduled Jobs that failed to run.

NOTE: These scripts require Python version 2.7.3 and access to the
desired Splunk server to run as expected.

===============================================================================================
Dependencies
===============================================================================================
1. easy-install - Not  a direct dependency, but is required to install the actual dependencies.
   This may or may not already come pre-installed with Python. Check the 'Scripts' folder,
   likely located at C:\Python27\Scripts.
   
   Download Link: http://pypi.python.org/pypi/setuptools#files
   
   Installation Instructions:
     a. Download easy_install
	 b. Run the executable file
	 c. Follow the Installation Wizard setup, install to default location.

	 
2. pytz - Accurate cross platform timezone calculations
   Download Link: http://pypi.python.org/pypi/pytz/
   
   Installation Instructions:
     a. Download pytz egg file, version 3.2 (pytz-2012j-py3.2.egg)
     	Note the download location of this file (ie "C:\Users\<USER>\Downloads\pytz-2012j-py3.2.egg")
	 b. Open a terminal and cd to the python scripts folder. This will likely be C:/Python27/Scripts.
	 c. run the following command:
          easy-install.exe [path to downloaded egg]
        For Example:
          easy-install.exe C:\Users\<USER>\Downloads\pytz-2012j-py3.2.egg

		  
3. Splunk Python SDK v1.0.0
   Download Link: http://dev.splunk.com/view/splunk-sdk-python/SP-CAAAEBB
   
   Installation Instructions:
     a. Download Splunk SDK, version 1.0.0
     	Note the download location of this file (ie "C:\Users\<USER>\Downloads\splunk-sdk-python")
	 b. Open a terminal and cd to the Splunk SDK folder.
	 c. run the following command:
          setup.py install
		OR
		  python setup.py install
		  
4. Python for Windows Extensions (pywin32) Build 218
   Download Link: http://sourceforge.net/projects/pywin32/
   Documentation Link: http://starship.python.net/~skippy/win32/
   
   Installation Instructions:
	 a. Download pywin32, Build 218 or later
	 b. Run the executable file
	 c. Follow the Installation Wizard setup, install to default location
   
NOTE: After downloading these dependencies, users MAY need to edit the import paths of
FailedJobsLogger.py, WebScraper.py, and other programs to point them to the location of the
newly downloaded dependencies so that they function as expected.
===============================================================================================



===============================================================================================
An overview of all the files included in this project:
===============================================================================================
+-- Splunk Scheduled Jobs Parser
	+-- webScraper
		+-- scraper src
			|- WebScraper.py					# The WebScraper source code
		|- __init__.py							# Package initilaization file (empty)
		|- test_getScheduledJobs.py				# Tests the getScheduledJobs method
		|- test_liveHTML.py						# Tests the getScheduledJobs method with live HTML
		|- test_printJobs.py					# Tests the printJobs method
		|- test_removeFunkyCharsFromLine.py		# Tests the removeFunkyCharsFromLine method
		|- test_removeTagsFromLine.py			# Tests the removeTagsFromLine method
		|- Tester_WebScraper.py					# *MAIN TEST FILE* - Creates test suites, runs all scraper tests
		|- testHTML0.html						# A sample HTML file used for testing
		|- testHTML1.html						# A sample HTML file used for testing
		|- testHTML2.html						# A sample HTML file used for testing
		|- testHTML3.txt						# A sample txt file used for testing	
	|- Main.py									# The main file used to log into Splunk server
	|- README.txt								# This file
	|- ScheduledJobs.html						# A sample txt file used for testing
	|- FailedJobsLogger.py						# The FailedJobsLogger source code
	|- Tester_JobsLogger.py						# *MAIN TEST FILE* - Tests jobs logger
	
===============================================================================================



===============================================================================================
Run tests togehter by running Tester_JobsLogger.py or Tester_WebScraper.py
===============================================================================================

To run Tester_JobsLogger cd to the directory containing the Splunk
Scheduled Jobs Parser folder, then enter the following:

	>> cd .../Splunk Scheduled Jobs Parser/
	>> Tester_JobsLogger

If successful, you'll recieve the following output:

	[Lots of Specific Text Output]
    ...
    -------------------------------
    Ran 64 tests in 3.070s
    
    OK
	
	
To run Tester_WebScraper cd to the directory containing the Splunk
Scheduled Jobs Parser folder, then enter the following:

	>> cd .../Splunk Scheduled Jobs Parser/
	>> cd webScraper
	>> Tester_WebScraper

If successful, you'll recieve the following output:

	[Lots of Specific Text Output]
    ...
    ----------------------------------------------------------------------
    Ran 43 tests in 6.842s
    
    OK

===============================================================================================