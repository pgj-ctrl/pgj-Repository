import paramiko

def rcmd(orders):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('127.0.0.1', username='root', password='123', port=22)
    ssh.exec_command(orders)
    stdin, stdout, stderr = ssh.exec_command(orders)
    out = stdout.read()
    err = stderr.read()
    xxx = stderr.read()
    print(out.decode())
    print(err.decode())
    print(xxx.decode())
    ssh.close()

if __name__ == '__main__':
    u = input('orders:')
    rcmd(u)