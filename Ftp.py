from ftplib import FTP
from ftplib import all_errors as ftp_errors


def ftp_test(logger, host: str, user: list = [], pwd: list = []):
    try:
        ftp = FTP(host)
        logger.info('FTP :: Connected to ' + host)
        if len(user) is not 0:
            for user_cur in user:
                try:
                    resp = ftp.login(user_cur, user.index(user_cur))
                    logger.info('FTP ::  user : ' + user_cur + '  ' + resp)
                except ftp_errors:
                    logger.error('FTP ::  user : ' + user_cur + ' - Connection failed')
    except:
        logger.error('FTP :: Connection to ' + host + ' failed')
