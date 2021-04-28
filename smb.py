import sys
import logging 
from impacket.examples import logger 
from impacket import smbserver, version 
from impacket.ntlm import compute_lmhash, compute_nthash 

if __name__ == '__main__': 
	print(version.BANNER)
	logger.init(True)
	logging.getLogger().setLevel(logging.INFO) #logging.DEBUG for debugging 
	comment = "personal"
	listenAddress= "0.0.0.0"
	listenPort = "7777"
	shareName = "PERSONAL"
	sharePath = "/home/pi/HoneySMB/smb/smbDrive" 
	username = "tcruise"
	password = "#########" # you could change the logon password to anything you prefer
	readOnly =  "yes"
	
	server = smbserver.SimpleSMBServer(listenAddress=listenAddress, listenPort=int(listenPort)) 
	server.addShare(shareName, sharePath, shareComment=comment, shareType='0', readOnly='Yes') 
	lmhash = compute_lmhash(password)
	nthash = compute_nthash(password) 
	server.setSMB2Support(True)
	server.addCredential(username, 0, lmhash, nthash) 
	server.setSMBChallenge('') 
	server.setLogFile("/home/pi/HoneySMB/smb.log") 
	server.start() 
	
