import getpass
import sys
import telnetlib
import time

###################################################################
# ffunction TELNET
###################################################################

def telnet(host):

    cmd_file = open('commandlist.txt', 'r')


    tn = telnetlib.Telnet(host)

    tn.read_until("Username: ")
    tn.write(user + "\r\n")
    tn.read_until("Password: ")
    tn.write(password + "\r\n")

    #tn.write("term len 0\n")
    #tn.write("sh int desc\n")
    #tn.write("logout" + "\n")

    for cmd in cmd_file:
        tn.write(cmd.rstrip() + "\n")

    file = open("telnet_out_." + date + ".txt", "a")
    file.write("+++++++++++++++++++++++++++++++++++++ " + host + " +++++++++++++++++++++++++++++++++++++" + "\n" + tn.read_all() + "\n\n\n\n\n")
    file.close()




###################################################################
# MAIN
###################################################################

input_file = open('hostlist.txt', 'r')
date = time.strftime("%Y%m%d-%H%M%S")

user = raw_input("Enter your remote account: ")
password = getpass.getpass()

for i in input_file:
    telnet(i.rstrip())
