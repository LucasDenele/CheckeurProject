from socket import timeout

try:
    import paramiko
except:
    from os import system
    system('pip install --user paramiko')
    import paramiko

def ssh_test(logger, host: str, user: list = [], pwd: list = [], sftp: bool = False):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    for user_cur in user:
        try:
            if pwd[user.index(user_cur)] is None or pwd[user.index(user_cur)] == '':
                client.connect(host, username=user_cur, timeout=1)
            else:
                client.connect(host, username=user_cur, password=pwd[user.index(user_cur)], timeout=1)
            logger.info(('SFTP ::  user :  ' if sftp else 'SSH ::  user :  ') + user_cur + ' - Authentification success')
        except paramiko.ssh_exception.AuthenticationException:
            logger.error(('SFTP ::  user :  ' if sftp else 'SSH ::  user :  ')+user_cur+' - Authentification failed')
        except paramiko.ssh_exception.NoValidConnectionsError:
            logger.error(('SFTP ::  Cannot connect to server : ' if sftp else 'SSH ::  Cannot connect to server : ') + host)
        except timeout:
            logger.error('SFTP ::  Connection timeout' if sftp else 'SSH ::  Connection timeout')
        finally:
            client.close()