from socket import timeout

try:
    import paramiko
except:
    from os import system
    system('pip install paramiko')
    import paramiko

def ssh_test(logger, host: str, user: list = [], pwd: list = []):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    for user_cur in user:
        try:
            if pwd[user.index(user_cur)] is None or pwd[user.index(user_cur)] == '':
                client.connect(host, username=user_cur, timeout=1)
            else:
                client.connect(host, username=user_cur, password=pwd[user.index(user_cur)], timeout=1)
            logger.info('SSH ::  user :  ' + user_cur + ' - Authentification success')
        except paramiko.ssh_exception.AuthenticationException:
            logger.error('SSH ::  user :  '+user_cur+' - Authentification failed')
        except timeout:
            logger.error('SSH ::  Connection timeout')
        finally:
            client.close()