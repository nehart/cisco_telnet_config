import telnetlib

def telnet(host):

    cmd_file = open('commandlist.txt', 'r')


    tn = telnetlib.Telnet(host)

    tn.read_until("Username: ")
    tn.write(user + "\r\n")
    tn.read_until("Password: ")
    tn.write(password + "\r\n")

    for cmd in cmd_file:
        tn.write(cmd.rstrip() + "\n")

    file = open("telnet_out_." + date + ".txt", "a")
    file.write("+++++++++++++++++++++++++++++++++++++ " + host + " +++++++++++++++++++++++++++++++++++++" + "\n" + tn.read_all() + "\n\n\n\n\n")
    file.close()