import paramiko

#default settings
hostname = '145.129.106.104'
port = 22
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
     input1 = raw_input("#~")
     stdin, stdout, stderr = s.exec_command(input1)
     print stdout.read()
    
     if input1 == "shutdown":
      s.close()
     else:
      return(mainloop())

    mainloop()
