import paramiko

#建立SSHClient
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#連接伺服器
ssh.connect(hostname='bandit.labs.overthewire.org', port=2220, username='bandit2', password='263JGJPfgU6LtdEvgfWU1XP5yac29mFx')

#查看檔案
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read().decode())
#用空格字元開啟檔案
stdin, stdout, stderr = ssh.exec_command('cat spaces\ in\ this\ filename')
print(stdout.read().decode())

#關閉伺服器
ssh.close()