import paramiko

#default settings
hostname = '192.168.2.22'
port = 22
portnum = '22'
username = 'root'
password = 'toor'



#truly no idee what it means
if __name__ == "__main__":
    #sshclient conection & error logs
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.load_system_host_keys()
    try:
     s.connect(hostname, port, username, password)
    except:
     print"ERROR: connection fail"

    def mainloop():
     input1 = raw_input((hostname) + "@" + (portnum) + "#~")
     try:
      stdin, stdout, stderr = s.exec_command(input1)
      print stdout.read()
     except:
       if input1 == 'start connection':
        print"######################################### conection establist"
       else:
        print"ERROR: is youre connection establist?"
     if input1 == "quit connection":
      s.close()
     if input1 == "start connection":
       try:
         s.connect(hostname, port, username, password)
       except:
         print"ERROR: connection fail"
     if input1 == '--help':
      print"help menu"
      print"to start connection type: start connection"
      print"to stop connection type: quit connection"
      return(mainloop())
     else:
      return(mainloop())


    mainloop()
