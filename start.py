# ----------------------------
# Part 1 - import library
# 			and constant value
# ----------------------------

# imports:
import json
import logging
from logging.handlers import RotatingFileHandler
import begin
import requests

# constants:
LOGGER = 0


# ----------------------------
# Part 2 - all functions
#
# ----------------------------

def test_co(access_token: str, protocole: str, users: list, passwords: list):
    global LOGGER
    if None != users:
        for i in range(0, len(users)):
            print("Connection at " + access_token + " with " + protocole + " / user : " + users[i] +
                  " ; password : " + passwords[i])
    else:
        print("Connection at " + access_token + " with " + protocole)
    if "http" == protocole:
        #A mettre dans le switch pour http :
        if not users:
            http = requests.get(access_token)
            if( 200 <= http.status_code and 300 >= http.status_code):
                LOGGER.info("Connection on "+access_token+" is ok")
            else:
                LOGGER.error("Connection on"+access_token+" failed")
        else:
            for i in range(len(users)):
                http = requests.get(access_token, auth=(users[i], passwords[i]))
                if( 200 <= http.status_code and 300 >= http.status_code):
                    LOGGER.info("Connection on "+access_token+" is ok")
                else:
                    LOGGER.error("Connection on"+access_token+" failed")


        


def create_loggers(file_localisation_all: str, file_localisation_error: str):
    """ Create the logger for all information"""

    # Create the logging objects
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create the logs format
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    # Do handler for the error logger
    file_handler = RotatingFileHandler(file_localisation_error, 'a', 1000000, 1)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Create the handler, with a security space. The log file will have 1Mo max size
    file_handler = RotatingFileHandler(file_localisation_all, 'a', 1000000, 1)
    # Apply the handler to the logger
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def json_parse(file: dict):
    """ Parse the json file to get the informations for the connections"""
    global LOGGER

    # ==== Errors handler ====
    # Check if the access_token has given and is right type
    if None ==   file.get('access_token'):
        if None == file.get('name'):
            LOGGER.error("KeyError : 'access_token' has not been given, machine has no name")
        else:
            LOGGER.error("KeyError : 'access_token' has not been given in " + file.get('name'))
        return
    if not isinstance(file.get('access_token'), str):
        if None == file.get('name'):
            LOGGER.error("FormatError : 'access_token' must be a string, machine has no name")
        else:
            LOGGER.error("FormatError : 'access_token' must be a string in " + file.get('name'))
        return
    # Check if the protocole has given and is right type
    if None == file.get("protocole"):
        if None == file.get('name'):
            LOGGER.error("KeyError : 'protocole' has not been given, machine has no name")
        else:
            LOGGER.error("KeyError : 'protocole' has not been given in " + file.get('name'))
        return
    if not isinstance(file.get('protocole'), str):
        if None == file.get('name'):
            LOGGER.error("FormatError : 'protocole' must be a string, machine has no name")
        else:
            LOGGER.error("FormatError : 'protocole' must be a string in " + file.get('name'))
        return

    # Check if there are the same numbers of user names and passwords and are right type
    if None != file.get("users") or None != file.get("passwords"):
        if len(file["users"]) > len(file["passwords"]):
            if None == file.get('name'):
                LOGGER.error("FormatError : missing " + str(len(file["users"]) - len(file["passwords"])) +
                             " password(s), machine has no name")
            else:
                LOGGER.error("FormatError : missing " + str(len(file["users"]) - len(file["passwords"])) +
                             " password(s) in " + file.get('name'))
            return
        if len(file["passwords"]) > len(file["users"]):
            if None == file.get('name'):
                LOGGER.error("FormatError : missing " + str(len(file["passwords"]) - len(file["users"])) +
                             " user name(s), machine has no name")
            else:
                LOGGER.error("FormatError : missing " + str(len(file["passwords"]) - len(file["users"])) +
                             " user name(s) in " + file.get('name'))
            return
        if not isinstance(file.get('passwords'), list):
            if None == file.get('name'):
                LOGGER.error("FormatError : 'passwords' must be a string, machine has no name")
            else:
                LOGGER.error("FormatError : 'passwords' must be a string in " + file.get('name'))
            return
        if not isinstance(file.get('users'), list):
            if None == file.get('name'):
                LOGGER.error("FormatError : 'users' must be a string, machine has no name")
            else:
                LOGGER.error("FormatError : 'users' must be a string in " + file.get('name'))
            return
    else:
        test_co(file["access_token"], file["protocole"], [], [])
        return
    LOGGER.info("HelloWorld")
    test_co(file["access_token"], file["protocole"], file["users"], file["passwords"])


def start_connections(json_localisation: str):
    """ Return a list with the informations for the connections to do"""

    # Open the file
    with open(json_localisation) as checkeur_data:
        data = checkeur_data.read()
    # Parse the bloc to have the informations
    json.loads(data, object_hook=json_parse)


# ----------------------------
# Part 3 - file entry
#
# ----------------------------

@begin.convert(access_file=str, log_all_file=str, log_error_file=str)
@begin.start
def run(access_file, log_all_file, log_error_file):
    global LOGGER
    LOGGER = create_loggers(log_all_file, log_error_file)
    start_connections(access_file)
