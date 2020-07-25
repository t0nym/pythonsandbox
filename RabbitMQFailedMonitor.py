#!/usr/bin/env python
import subprocess
import re

bashCommand = "rabbitmqctl list_queues"
queueNames = ["baf_failed_"] #queues containing these strings will be monitored
exclusion = "retried" #Queues with this string will be excluded from monitoring
okLevel = 0
warningLevel = 7500

process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

def PrintOutput(status = 0, checkName = '', queueLength = '-', description = ''):
	#keeping track of the queueLength and queueName for now but not exposing them
	###   print "{0} {1}".format(status, description)
	print "{0} {1} - {2}".format(status, checkName, description)
	
for queueName in queueNames:

	###	print("\nqueueName is %s\n" % queueName)
	###	print("\tOutput is %s\n" % output)
	###	print("\tError is %s\n\n`" % error)
		
	for line in output.split("\n"):
		if "Listing queues" not in line and "...done" not in line and line:

			###	print("%s is line... \n" % line)

			qName = line.split()[0] 	

			###	print("QName is now %s..." % qName)

			perfdata = int(line.split()[1])

			###if queueName in qName and exclusion not in qName:
			if queueName in qName and exclusion not in qName:
				if perfdata <= okLevel:
					description = 'OK - RabbitMQ queue size is under ' + str(okLevel) + ' items' 
					status = 0
				elif perfdata > okLevel and perfdata <= warningLevel:
					description = 'WARNING - RabbitMQ queue size is over ' + str(okLevel) + ' items'
					status = 1
				elif perfdata > warningLevel:
					description = 'CRITICAL - RabbitMQ queue size is over ' + str(warningLevel) + ' items' 
					status = 2
				else:
					description = 'UNKNOWN - RabbitMQ contains an unknown number of items'
					status = 3
			        ###	 print("%s is status " % status)		
			        ###	print("%s is qName " % qName)		
			        ###	print("%s is perfdata " % perfdata)		
			        ###	print("%s is description " % description)		
				PrintOutput(status, qName, perfdata, description)
