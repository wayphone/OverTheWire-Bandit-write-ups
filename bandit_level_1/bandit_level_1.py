import paramiko

#建立SSHClient
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#連接伺服器
ssh.connect(hostname='bandit.labs.overthewire.org', port=2220, username='bandit1', password='ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If')

#查看檔案
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read().decode())
#開啟檔案
stdin, stdout, stderr = ssh.exec_command('cat < -')
print(stdout.read().decode())

#關閉伺服器
ssh.close()