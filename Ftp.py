from ftplib import FTP
from ftplib import all_errors as ftp_errors


def ftp_test(logger, host: str, user: list = [], pwd: list = []):
    try:
        ftp = FTP(host)
        print('marche')
        logger.info('FTP :: Connected to ' + host)
        if len(user) is not 0:
            for user_cur in user:
                try:
                    resp = ftp.login(user_cur, user.index(user_cur))
                    logger.info('FTP ::  user : ' + user_cur + '  ' + resp)
                except ftp_errors:
                    logger.error('FTP ::  user : ' + user_cur + ' - Connection failed')
    except:
        print('marche pas')
        logger.error('FTP :: Connection to ' + host + ' failed')


if __name__ == '__main__':
    ftp_test()
