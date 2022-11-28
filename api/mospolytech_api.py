# --------------------------------------------------------------------------------------------------------------------#
# ███╗   ███╗ ██████╗ ███████╗██████╗  ██████╗ ██╗  ██╗   ██╗████████╗███████╗ ██████╗██╗  ██╗     █████╗ ██████╗ ██╗ #
# ████╗ ████║██╔═══██╗██╔════╝██╔══██╗██╔═══██╗██║  ╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔══██╗██║ #
# ██╔████╔██║██║   ██║███████╗██████╔╝██║   ██║██║   ╚████╔╝    ██║   █████╗  ██║     ███████║    ███████║██████╔╝██║ #
# ██║╚██╔╝██║██║   ██║╚════██║██╔═══╝ ██║   ██║██║    ╚██╔╝     ██║   ██╔══╝  ██║     ██╔══██║    ██╔══██║██╔═══╝ ██║ #
# ██║ ╚═╝ ██║╚██████╔╝███████║██║     ╚██████╔╝███████╗██║      ██║   ███████╗╚██████╗██║  ██║    ██║  ██║██║     ██║ #
# ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚══════╝╚═╝      ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝ #
# author: https://t.me/rand0lphc                                                                          version 2.0 #
# ------------------------------------------------------------------------------------------------------------------- #


import hashlib
import json

import requests
from bs4 import BeautifulSoup as bs


class API:
    """
        DESCRIPTION
            * API for working with the services of the Moscow Polytechnic University;
            * https://mospolytech.ru/;

        ATTRIBUTES
            * there are no public attributes;

        ARGS
            * (optional) user_agent (str): string that lets servers identify the application,
            default is __DEFAULT_USER_AGENT;

        METHODS
            * get_group_names(self) -> list;
    """

    # private attributes for API operation
    __URL = "https://rasp.dmami.ru/"
    __DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                           "Chrome/86.0.4240.75 Safari/537.36"

    def __init__(self, user_agent: str = __DEFAULT_USER_AGENT) -> None:
        """
        DESCRIPTION
            * initializes the API object;

        ARGS
            * (optional) user_agent (str): string that lets servers identify the application,
            default is __DEFAULT_USER_AGENT;

        RETURNS
            * there are no return;

        ERRORS
            * there are no custom errors;
        """

        # setting headers
        self.headers = {
            "referer": self.__URL,
            "user-agent": user_agent
        }

    @staticmethod
    def __check_status_code(code: int) -> None:
        """
        DESCRIPTION
            * checks the correctness of the response status code;

        ARGS
            * (required) code (int): response status code;

        RETURNS
            * there are no return;

        ERRORS
            * ConnectionError() - if there is a problem with the connection;
        """

        # checking status code
        if code != 200:
            raise requests.ConnectionError(
                f"Expected status code 200, but got {code}."
            )

    def get_group_names(self) -> list:
        """
        DESCRIPTION
            * returns a list of group names;

        ARGS
            * there are no args;

        RETURNS
            * group_names (list of strs): list of group names that are existing;

        ERRORS
            * ConnectionError() - if there is a problem with the connection;
        """

        # making request
        r_url = self.__URL + "groups-list.json"
        r = requests.get(url=r_url, headers=self.headers)

        # checking status code
        self.__check_status_code(r.status_code)

        # loading content to dict
        data = json.loads(r.content)

        # returning sorted list of group names
        return sorted([name for name in data["groups"]])


if __name__ == "__main__":
    m_api = API()
    list_gn = m_api.get_group_names()
    print(list_gn)
