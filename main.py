import getpass
import sys
import time

###################################################################
# function TELNET
###################################################################

import lib.lib_telnet




###################################################################
# MAIN
###################################################################

input_file = open('hostlist.txt', 'r')
date = time.strftime("%Y%m%d-%H%M%S")

user = raw_input("Enter your remote account: ")
password = getpass.getpass()

for i in input_file:
    lib.lib_telnet.telnet(i.rstrip())