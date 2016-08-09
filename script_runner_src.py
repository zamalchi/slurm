if (__name__ == "__main__"):
	print("Run webapp through wrapper.")
	print("Exiting...")
	exit()

### PACKAGES ###########################################################################################

import os
import sys
import commands

### APACHE #############################################################################################

os.chdir(os.path.dirname(__file__))
sys.path.insert(1, os.path.dirname(__file__))

### IMPORTS ############################################################################################

from bottle import Bottle, route, run, request, response, get, post

### HELPER METHODS ##################################################################################### 

def getHostParam(request):
	return request.query.host or None

def hostNotSuppliedMsg():
	return "Please enter the query parameter: 'host'"

########################################################################################################
########################################################################################################
########################################################################################################

#
#
#
#
#
#
#
#

########################################################################################################
######################################  	NODE ROUTES START	 ###########################################
########################################################################################################

@route('/reinstall')
def reinstall_node():
	host = getHostParam(request)
	if host:
		result = commands.getstatusoutput('./scripts/reinstall ' + host)
		return result
	
	return hostNotSuppliedMsg()

########################################################################################################
########################################################################################################

@route('/default')
def default_node():
	host = getHostParam(request)
	if host:
		result = commands.getstatusoutput('./scripts/default ' + host)
		return result

	return hostNotSuppliedMsg()

########################################################################################################
########################################################################################################

@route('/slurm')
def slurm_node():
	host = getHostParam(request)
	if host:
		result = "getting slurm for {0}...".format(host)
		return result

	return hostNotSuppliedMsg()

########################################################################################################
######################################  	NODE ROUTES END	 #############################################
########################################################################################################
