import paramiko

#建立SSHClient
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#連接伺服器
ssh.connect(hostname='bandit.labs.overthewire.org', port=2220, username='bandit0', password='bandit0')

#執行命令&輸出結果
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read().decode())
stdin, stdout, stderr = ssh.exec_command('cat readme')
print(stdout.read().decode())

#關閉伺服器
ssh.close()