# --------------------------------------------------------------------------------------------------------------------#
# ███╗   ███╗ ██████╗ ███████╗██████╗  ██████╗ ██╗  ██╗   ██╗████████╗███████╗ ██████╗██╗  ██╗     █████╗ ██████╗ ██╗ #
# ████╗ ████║██╔═══██╗██╔════╝██╔══██╗██╔═══██╗██║  ╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔══██╗██║ #
# ██╔████╔██║██║   ██║███████╗██████╔╝██║   ██║██║   ╚████╔╝    ██║   █████╗  ██║     ███████║    ███████║██████╔╝██║ #
# ██║╚██╔╝██║██║   ██║╚════██║██╔═══╝ ██║   ██║██║    ╚██╔╝     ██║   ██╔══╝  ██║     ██╔══██║    ██╔══██║██╔═══╝ ██║ #
# ██║ ╚═╝ ██║╚██████╔╝███████║██║     ╚██████╔╝███████╗██║      ██║   ███████╗╚██████╗██║  ██║    ██║  ██║██║     ██║ #
# ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚══════╝╚═╝      ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝ #
# author: https://t.me/rand0lphc                                                                          version 3.0 #
# ------------------------------------------------------------------------------------------------------------------- #


import json
from hashlib import md5

import requests


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
        * get_groups() -> list[str];
        * get_students(list_groups: list = None) -> list[str];
        * def get_schedule(group: str) -> dict;
    """

    # private attributes for API operations
    __DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                           "Chrome/86.0.4240.75 Safari/537.36"
    __URLS = {
        "referer": "https://rasp.dmami.ru/",
        "groups": "https://rasp.dmami.ru/groups-list.json",
        "students": "https://e.mospolytech.ru/old/lk_api_mapp.php",
        "schedule": "https://rasp.dmami.ru/site/group-html"
    }
    __HASH_SALT = "}{YWHksld#52673$3*9dNG"

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
            "referer": self.__URLS["referer"],
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
            * ConnectionError(): if there is a problem with the connection;
        """

        # checking status code
        if code != 200:
            raise requests.ConnectionError(
                f"Expected status code 200, but got {code}."
            )

    def __create_token(self, group: str) -> str:
        """
        DESCRIPTION
            * creates a token (md5 hash-string) for the given group;

        ARGS
            * (required) group (str): name of the group;

        RETURNS
            * token (str): token for the given group;

        ERRORS
            * there are no custom errors;
        """

        # creating token (hash object)
        string = group + self.__HASH_SALT
        token = md5(md5(string.encode()).hexdigest().encode())

        # returning created token (str object)
        return token.hexdigest()

    def get_groups(self) -> list[str]:
        """
        DESCRIPTION
            * returns a list of group names;

        ARGS
            * there are no args;

        RETURNS
            * groups (list[str]): sorted list of group names that are existing;

        ERRORS
            * ConnectionError(): if there is a problem with the connection;
        """

        # making request
        r_url = self.__URLS["groups"]
        r = requests.get(url=r_url, headers=self.headers)

        # checking status code
        self.__check_status_code(r.status_code)

        # loading content to dict
        data = json.loads(r.content)

        # returning sorted list of group names
        return sorted([name for name in data["groups"]])

    def get_students(self, list_groups: list = None) -> list[str]:
        """
        DESCRIPTION
            * returns a list of students for the given groups;

        ARGS
            * (optional) list_groups (list[str]): list of group names,
            default is None - search across all groups;

        RETURNS
            * students (list[str]): sorted list of students for the given groups;

        ERRORS
            * ConnectionError(): if there is a problem with the connection;
        """

        # forming group names list
        if list_groups is None:
            list_groups = self.get_groups()

        # creating list of students
        list_students = []

        # getting students
        for group in list_groups:

            # creating token (str object)
            token = self.__create_token(group)

            # making request
            r_url = self.__URLS["students"] + \
                f"?group={group.replace(' ', '%20')}&token={token}"
            r = requests.get(url=r_url, headers=self.headers)
            content = r.content.decode("utf-8")

            # checking status code
            self.__check_status_code(r.status_code)

            # loading content to list of students
            list_students += json.loads(content)

        # returning sorted list of students
        return sorted(list_students)

    def get_schedule(self, group: str) -> dict:
        """
        DESCRIPTION
            * returns a dict of the raw schedule;

        ARGS
            * (required) group (str): name of the group;

        RETURNS
            * schedule (dict): dict containing raw schedule information;

        ERRORS
            * ConnectionError(): if there is a problem with the connection;
        """

        # making request
        r_url = self.__URLS["referer"] + \
            f"site/group?group={group.replace(' ', '%20')}"
        r = requests.get(url=r_url, headers=self.headers)

        # checking status code
        self.__check_status_code(r.status_code)

        # decoding content
        content = r.content.decode("utf-8")

        # checking correctness of schedule (1)
        SCHEDULE_NOT_EXIST = "Еще не готово расписание для группы"
        if content == SCHEDULE_NOT_EXIST:
            raise ValueError(
                f"The schedule for the '{group}' group does not exist."
            )

        # loading content to dict
        data = json.loads(content)

        # checking correctness of schedule (2)
        SCHEDULE_EMPTY = "Не нашлось расписание для группы"
        if "message" in data:
            if data["message"] == SCHEDULE_EMPTY:
                raise ValueError(
                    f"The schedule for the '{group}' group is empty."
                )

        # creating raw schedule
        schedule = {
            "group": group,
            "type": "evening" if data["group"]["evening"] else "morning",
            "dates": [".".join(d.split("-")[::-1]) for d in [data["group"]["dateFrom"], data["group"]["dateTo"]]],
            "grid": []
        }

        # filling grid
        for k_day in data["grid"]:
            day = []
            for k_pair in data["grid"][k_day]:
                pair = {"subjects": []}
                for raw_sbj in data["grid"][k_day][k_pair]:
                    # checking type & creating sbj["dates"]
                    if len(list(data["grid"].keys())[0]) == 10:
                        dates = [".".join(d.split("-")[::-1])
                                 for d in [k_day] * 2]
                    else:
                        dates = [".".join(d.split("-")[::-1])
                                 for d in [raw_sbj["df"], raw_sbj["dt"]]]
                    # creating sbj
                    sbj = {
                        "title": raw_sbj["sbj"].strip(),
                        "type": raw_sbj["type"],
                        "teachers": [t.strip() for t in raw_sbj["teacher"].split(",")],
                        "location": raw_sbj["location"].strip(),
                        "rooms": [r.strip() for r in raw_sbj["shortRooms"]],
                        "dates": dates
                    }
                    pair["subjects"].append(sbj)
                day.append(pair)
            schedule["grid"].append(day)

        # returnig raw schedule
        return schedule


if __name__ == "__main__":
    pass
