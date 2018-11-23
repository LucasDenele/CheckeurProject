try:
    import requests
except:
    from os import system
    system('pip install requests')
    import requests



def http_test(logger, host: str, user: list = [], pwd: list = []):
    if not user:
        http = requests.get(host)
        if (200 <= http.status_code and 300 >= http.status_code):
            logger.info("HTTP/S :: Connection on " + host + " is ok")
        else:
            logger.error("HTTP/S :: Connection on" + host + " failed")
    else:
        for i in range(len(user)):
            http = requests.get(host, auth=(user[i], pwd[i]))
            if (200 <= http.status_code and 300 >= http.status_code):
                logger.info("HTTP/S :: Connection on " + host + " is ok")
            else:
                logger.error("HTTP/S :: Connection on" + host + " failed")