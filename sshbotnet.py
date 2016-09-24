import paramiko
hostname1 = '145.129.106.104'
port1 = 22
username1 = 'root'
password1 = 'toor'


hostname2 = '145.129.106.104'
port2 = 22
username2 = 'root'
password2 = 'toor'

endline = "\n"

def ignore():
 pass


if hostname1 == hostname2:
 print"[-] ssh1 has same addrs as ssh2 : " + (endline) + "ssh1: " + (hostname1) + (endline) + "ssh2: " + (hostname2) + (endline)
else:
 ignore()







paramiko.util.log_to_file('paramiko.log')

#bot connect

try:
    ssh1 = paramiko.SSHClient()
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh1.load_system_host_keys()
    ssh1.connect(hostname1, port1, username1, password1)
except:
    print"[-] error with ssh1:" + (hostname1)

#bot connect

try:
    ssh2 = paramiko.SSHClient()
    ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh2.load_system_host_keys()
    ssh2.connect(hostname2, port2, username2, password2)
except:
    print"[-] error with ssh2:" + (hostname2)


def mainloop():
     maininput = raw_input("#~")





     stdin, stdout, stderr = ssh1.exec_command(maininput)
     print stdout.read()
 
     print"##### bot 2 #########################################"

     stdin, stdout, stderr = ssh2.exec_command(maininput)
     print stdout.read()

     if maininput == "quit connection":
      ssh1.close()
      ssh2.close()
     else:
      return(mainloop())



mainloop()

