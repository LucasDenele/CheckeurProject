# ----------------------------
# Part 1 - import library
# 			and constant value
# ----------------------------

# imports:
import json


# constants:

# ----------------------------
# Part 2 - all functions
#
# ----------------------------
def json_parse(file: dict):
    """ Parse the json file to get the informations for the connections"""

    # ==== Errors handler ====
    # Check if the access_token has given
    if None == file.get('access_token'):
        raise NameError("KeyError : 'access_token' has not been given")
    # Check if the access_token has given
    if None == file.get("protocole"):
        raise NameError("KeyError : 'protocole' has not been given")
    # Check if the access_token has given
    if None == file.get("users"):
        raise NameError("KeyError : 'users' has not been given")
    # Check if the access_token has given
    if None == file.get("passwords"):
        raise NameError("KeyError : 'passwords' has not been given")
    # Check if there are the same numbers of user names and passwords
    if len(file["users"]) > len(file["passwords"]):
        raise NameError("FormatError : missing " + str(len(file["users"]) - len(file["passwords"])) + " password(s)")
    if len(file["passwords"]) > len(file["users"]):
        raise NameError("FormatError : missing " + str(len(file["passwords"]) - len(file["users"])) + " user name(s)")

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
