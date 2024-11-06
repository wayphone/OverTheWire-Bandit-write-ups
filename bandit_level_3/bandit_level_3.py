import paramiko

#建立SSHClient
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#連接伺服器
ssh.connect(hostname='bandit.labs.overthewire.org', port=2220, username='bandit3', password='MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx')

#查看檔案
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read().decode())
#進入inhere
stdin, stdout, stderr = ssh.exec_command('cd inhere')
print(stdout.read().decode())

#查找隱藏檔案
stdin, stdout, stderr = ssh.exec_command('ls -la')
print(stdout.read().decode())

#開啟隱藏檔案
stdin, stdout, stderr = ssh.exec_command('cat ...Hiding-From-You')
print(stdout.read().decode())

#關閉伺服器
ssh.close()