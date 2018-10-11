# ----------------------------
# Part 1 - import library
# 			and constant value
# ----------------------------

# imports:
import json
import logging
from logging.handlers import RotatingFileHandler


# constants:
LOGGER = 0


# ----------------------------
# Part 2 - all functions
#
# ----------------------------
def create_loggers(file_localisation_all: str, file_localisation_error: str):
    """ Create the logger for all information"""

    # Create the logging objects
    logger = logging.getLogger()

    # Create the logs format
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    # Create the handler, with a security space. The log file will have 1Mo max size
    file_handler = RotatingFileHandler(file_localisation_all, 'a', 1000000, 1)

    # Apply the handler to the logger
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Do handler for the error logger
    file_handler = RotatingFileHandler(file_localisation_error, 'a', 1000000, 1)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def json_parse(file: dict):
    """ Parse the json file to get the informations for the connections"""

    # ==== Errors handler ====
    # Check if the access_token has given
    if None == file.get('access_token'):
        LOGGER.error("KeyError : 'access_token' has not been given")
    # Check if the access_token has given
    if None == file.get("protocole"):
        LOGGER.error("KeyError : 'protocole' has not been given")
    # Check if the access_token has given
    if None == file.get("users"):
        LOGGER.error("KeyError : 'users' has not been given")
    # Check if the access_token has given
    if None == file.get("passwords"):
        LOGGER.error("KeyError : 'passwords' has not been given")
    # Check if there are the same numbers of user names and passwords
    if len(file["users"]) > len(file["passwords"]):
        LOGGER.error("FormatError : missing " + str(len(file["users"]) - len(file["passwords"])) + " password(s)")
    if len(file["passwords"]) > len(file["users"]):
        LOGGER.error("FormatError : missing " + str(len(file["passwords"]) - len(file["users"])) + " user name(s)")

    # ==== Return ===
    # return the different parts of the needed informations
    return file["access_token"], file["protocole"], file["users"], file["passwords"]


def get_connections_informations(json_localisation: str):
    """ Return a list with the informations for the connections to do"""

    check_list = list()
    # Open the file
    with open(json_localisation) as checkeur_data:
        data = checkeur_data.read()
        # Parse the bloc to have the informations
        check_list.append(json.loads(data, object_hook=json_parse))
    return check_list


# ----------------------------
# Part 3 - main entry
# ----------------------------

if __name__ == "__main__":
    """
    """
    LOGGER = create_loggers("D:/ISEN/Python/Checkeur/CheckeurProject/logAll.txt", "D:/ISEN/Python/Checkeur/CheckeurProject/logError.txt")
    get_connections_informations("D:/ISEN/Python/Checkeur/CheckeurProject/checkeur.json")