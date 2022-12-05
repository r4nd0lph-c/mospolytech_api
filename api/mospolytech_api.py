# --------------------------------------------------------------------------------------------------------------------#
# ███╗   ███╗ ██████╗ ███████╗██████╗  ██████╗ ██╗  ██╗   ██╗████████╗███████╗ ██████╗██╗  ██╗     █████╗ ██████╗ ██╗ #
# ████╗ ████║██╔═══██╗██╔════╝██╔══██╗██╔═══██╗██║  ╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔══██╗██║ #
# ██╔████╔██║██║   ██║███████╗██████╔╝██║   ██║██║   ╚████╔╝    ██║   █████╗  ██║     ███████║    ███████║██████╔╝██║ #
# ██║╚██╔╝██║██║   ██║╚════██║██╔═══╝ ██║   ██║██║    ╚██╔╝     ██║   ██╔══╝  ██║     ██╔══██║    ██╔══██║██╔═══╝ ██║ #
# ██║ ╚═╝ ██║╚██████╔╝███████║██║     ╚██████╔╝███████╗██║      ██║   ███████╗╚██████╗██║  ██║    ██║  ██║██║     ██║ #
# ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚══════╝╚═╝      ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝ #
# author: https://t.me/rand0lphc                                                                          version 2.2 #
# ------------------------------------------------------------------------------------------------------------------- #


from hashlib import md5
import json

import requests
import bs4
from bs4 import BeautifulSoup as bs


class DatetimeToolbox:
    """
    ...
    """

    __LOCALE_DATES = {
        "Янв": "", "Фев": "", "Мар": "", "Апр": "",
        "Май": "", "Июн": "", "Июл": "", "Авг": "",
        "Сен": "", "Окт": "", "Ноя": "", "Дек": ""
    }

    def __init__(self) -> None:
        """
        ...
        """

        pass


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
        * def get_groups() -> list[str];
        * def get_students(list_groups: list = []) -> list[str];
        * def get_schedule(group: str) -> dict;
    """

    # private attributes for API operation
    __DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                           "Chrome/86.0.4240.75 Safari/537.36"
    with open("api/config.json", "r", encoding="utf-8") as config_file:
        __CONFIG = json.load(config_file)

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
            "referer": self.__CONFIG["urls"]["referer"],
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
        string = group + self.__CONFIG["hash_salt"]
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
        r_url = self.__CONFIG["urls"]["groups"]
        r = requests.get(url=r_url, headers=self.headers)

        # checking status code
        self.__check_status_code(r.status_code)

        # loading content to dict
        data = json.loads(r.content)

        # returning sorted list of group names
        return sorted([name for name in data["groups"]])

    def get_students(self, list_groups: list = []) -> list[str]:
        """
        DESCRIPTION
            * returns a list of students for the given groups;

        ARGS
            * (optional) list_groups (list[str]): list of group names,
            default is [] - search across all groups;

        RETURNS
            * students (list[str]): sorted list of students for the given groups;

        ERRORS
            * ConnectionError(): if there is a problem with the connection;
        """

        # forming group names list
        if not list_groups:
            list_groups = self.get_groups()

        # creating list of students
        list_students = []

        # getting students
        for group in list_groups:

            # creating token (str object)
            token = self.__create_token(group)

            # making request
            r_url = self.__CONFIG["urls"]["students"] + \
                f"?group={group.replace(' ', '%20')}&token={token}"
            r = requests.get(url=r_url, headers=self.headers)
            content = r.content.decode("utf-8")

            # checking status code
            self.__check_status_code(r.status_code)

            # loading content to list of students
            list_students += json.loads(content)

        return sorted(list_students)

    def get_schedule(self, group: str) -> dict:
        """
        ...
        """

        def is_permanent(div_schedule: bs4.element.Tag) -> bool:
            """
            ...
            """

            # parsing schedule title
            title = div_schedule.find_all(
                "div", {"class": "schedule-day__title"}
            )[0].text

            # getting title.split() length
            # == 1: schedule without specific dates
            # != 1: schedule with specific dates
            length = len(title.split())

            # returning bool value: is permanent
            return True if length == 1 else False

        def str_clear(s: str) -> str:
            """
            ...
            """

            if not (ord(s[0].lower()) in range(ord("а"), ord("я") + 1)):
                s = s[1:]
            s = s.replace("_", "")
            return s.strip()

        # creating token (str object)
        token = self.__create_token(group)

        # making request
        r_url = self.__CONFIG["urls"]["schedule"] + \
            f"?group={group.replace(' ', '%20')}&token={token}"
        r = requests.get(url=r_url, headers=self.headers)
        content = r.content.decode("utf-8")

        # checking status code
        self.__check_status_code(r.status_code)

        # checking correctness of schedule (1)
        NULL_SCHEDULE_CONTENT = "Еще не готово расписание для группы"
        if content == NULL_SCHEDULE_CONTENT:
            raise ValueError(
                f"The schedule for the '{group}' group does not exist."
            )

        # getting scedule (div block) & list of days (div blocks)
        soup = bs(content, features="html.parser")
        div_schedule = soup.find("div", {"class": "schedule-week"})
        div_days = div_schedule.find_all("div", {"class": "schedule-day"})

        # checking correctness of schedule (2)
        if not div_days:
            raise ValueError(
                f"The schedule for the '{group}' group is empty."
            )

        # creating raw schedule
        schedule = {
            "group": group,
            "grid": None,
            "dates": None,
            "is_permanent": is_permanent(div_schedule)
        }

        # creating permanent (True) schedule
        if schedule["is_permanent"]:
            # filling grid
            grid = []
            for div_day in div_days:
                day = []
                div_pairs = div_day.find("div", {"class": "pairs"}).find_all(
                    "div", {"class": "pair"})
                for div_pair in div_pairs:
                    pair = {
                        "time": [t.strip() for t in div_pair.find("div", {"class": "time"}).text.split("-")],
                        "subjects": None
                    }
                    subjects = []
                    div_lessons = div_pair.find("div", {"class": "lessons"}).find_all(
                        "div", {"class": "schedule-lesson"})
                    for div_lesson in div_lessons:
                        raw_texts = div_lesson.find(
                            "div", {"class": "bold small"}
                        ).text.split("(")
                        sbj = {
                            "title":  raw_texts[0].split("(")[0].strip(),
                            "type": raw_texts[-1][:-1].strip(),
                            "teachers": [t.strip() for t in div_lesson.find("div", {"class": "teacher small"}).text.split(",")],
                            "location": [str_clear(l.text) for l in div_lesson.find_all("div", {"class": "schedule-auditory"})],
                            "dates": [d.strip() for d in div_lesson.find("div", {"class": "schedule-dates"}).text.split("-")]
                        }
                        subjects.append(sbj)
                    pair["subjects"] = subjects
                    day.append(pair)
                grid.append(day)
            schedule["grid"] = grid

        # creating permanent (False) schedule
        else:
            pass

        # returnig raw schedule
        return schedule


if __name__ == "__main__":
    m_api = API()

    # 201-721 | 183-211 | 215-632 | 206-999
    schedule = m_api.get_schedule("201-721")
    # print(schedule)
    with open("logs.json", "w", encoding="utf-8") as f:
        json.dump(schedule, f, ensure_ascii=False, indent=4)
