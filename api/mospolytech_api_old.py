# --------------------------------------------------------------------------------------------------------------------#
# ███╗   ███╗ ██████╗ ███████╗██████╗  ██████╗ ██╗  ██╗   ██╗████████╗███████╗ ██████╗██╗  ██╗     █████╗ ██████╗ ██╗ #
# ████╗ ████║██╔═══██╗██╔════╝██╔══██╗██╔═══██╗██║  ╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔══██╗██║ #
# ██╔████╔██║██║   ██║███████╗██████╔╝██║   ██║██║   ╚████╔╝    ██║   █████╗  ██║     ███████║    ███████║██████╔╝██║ #
# ██║╚██╔╝██║██║   ██║╚════██║██╔═══╝ ██║   ██║██║    ╚██╔╝     ██║   ██╔══╝  ██║     ██╔══██║    ██╔══██║██╔═══╝ ██║ #
# ██║ ╚═╝ ██║╚██████╔╝███████║██║     ╚██████╔╝███████╗██║      ██║   ███████╗╚██████╗██║  ██║    ██║  ██║██║     ██║ #
# ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚══════╝╚═╝      ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝ #
# author: https://t.me/rand0lphc                                                                          version 1.0 #
# ------------------------------------------------------------------------------------------------------------------- #

from datetime import datetime
import json
import requests


class Group:
    """
    [DESCRIPTION]
        * a class representing a study group of a university;
        * contains information about the group;

    [ATTRIBUTES]
        * name (str): code-name of the group;
        * year_study_start (int): year of study start;
        * education_form (str): education form [intramural, extramural, part-time];
        * academic_degree (str): academic degree [undergraduate-specialty, master, postgraduate];
        * index_number (int): index number of the group;

    [ARGS]
        * (required) group_name (str): code-name of the group;
        * (optional) available_group_names (list of strs): list of available group names,
        * - default is None (calls API().get_group_names());

    [METHODS]
        * there are no public methods;
    """

    def __init__(self, group_name: str, available_group_names: list = None) -> None:
        """
        [DESCRIPTION]
            * initializes the Group object;

        [ARGS]
            * (required) group_name (str): code-name of the group;
            * (optional) available_group_names (list of strs): list of available group names,
            * - default is None (calls API().get_group_names());

        [RETURNS]
            * there are no return;

        [ERRORS]
            * ConnectionError() - if there is a problem with the connection;
            * ValueError() - if group name is not in list of available group names;
        """

        # checking group name
        self.__check_group_name(group_name, available_group_names)

        # setting group name
        self.name = group_name

        # generating info about group based on group name
        self.__decompose()

    @staticmethod
    def __check_group_name(group_name: str, available_group_names: list = None) -> None:
        """
        [DESCRIPTION]
            * checks if a group with the given name exists;

        [ARGS]
            * (required) group_name (str): code-name of the group;
            * (optional) available_group_names (list of strs): list of available group names,
            * - default is None (calls API().get_group_names());

        [RETURNS]
            * there are no return;

        [ERRORS]
            * ConnectionError() - if there is a problem with the connection;
            * ValueError() - if group name is not in list of available group names;
        """

        # getting allowed group names (default is None -> slowly object creation)
        if available_group_names is None:
            available_group_names = API().get_group_names()

        # checking group name
        if group_name not in available_group_names:
            raise ValueError(f"The '{group_name}' group does not exist.")

    def __decompose(self) -> None:
        """
        [DESCRIPTION]
            * creates attributes of a group based on its name;

        [ARGS]
            * there are no args;

        [RETURNS]
            * there are no return;

        [ERRORS]
            * there are no custom errors;
        """

        # TODO: fill in the values of the codes
        # codes info for decompose
        CODES = {
            "1": {"academic_degree": "undergraduate-specialty", "education_form": "intramural"},
            "2": {"academic_degree": "", "education_form": "part-time"},
            "3": {"academic_degree": "", "education_form": "extramural"},
            "4": {"academic_degree": "master", "education_form": "intramural"},
            "5": {"academic_degree": "master", "education_form": "part-time"},
            "6": {"academic_degree": "master", "education_form": "extramural"},
            "7": {"academic_degree": "", "education_form": ""},
            "8": {"academic_degree": "", "education_form": ""},
            "9": {"academic_degree": "", "education_form": ""},
            "А": {"academic_degree": "postgraduate", "education_form": ""}  # cyrillic symbol "А"
        }

        # filling attributes
        code = self.name[2]
        self.year_study_start = int("20" + self.name[0:2])
        self.education_form = CODES[code]["education_form"] if code in CODES else None
        self.academic_degree = CODES[code]["academic_degree"] if code in CODES else None
        self.index_number = int((self.name + " ")[6:(self.name + " ").find(" ")])

    def __str__(self) -> str:
        """
        [DESCRIPTION]
            * magic method;
            * presents class information in a human-readable form;

        [RETURNS]
            * representation (str): human-readable representation;
        """

        # returning class representation
        return f"Group(" \
               f"name: {self.name}, " \
               f"year_study_start: {self.year_study_start}, " \
               f"education_form: {self.education_form}, " \
               f"academic_degree: {self.academic_degree}, " \
               f"index_number: {self.index_number})"

    def __repr__(self) -> str:
        """
        [DESCRIPTION]
            * magic method;
            * presents class information in a form for debugging;

        [RETURNS]
            * self.__str__() (str): human-readable representation;
        """

        # returning class representation
        return self.__str__()


class Schedule:
    """
    [DESCRIPTION]
        * a class representing a schedule of a study group of a university;
        * contains information about the schedule;

    [ATTRIBUTES]
        * TIME_SECTIONS (dict): time sections for different forms of education;
        * body (list of lists): list for clear representing academic days ([] if is empty);
        * date_interval (dict): dictionary of info about date interval of the given schedule (None if is empty);

    [ARGS]
        * (required) group_name (str): code-name of the group;
        * (optional) raw_schedule (list of lists): result[0] of API().get_schedule_raw(group_name),
        * - default is None (calls API().get_schedule_raw(group_name));
        * (optional) date_interval (dict): result[1] of API().get_schedule_raw(group_name),
        * - default is None (calls API().get_schedule_raw(group_name));

    [METHODS]
        * get_day(self, date_str: str) -> list;
    """

    # time sections for different forms of education
    TIME_SECTIONS = {
        "day_form": [
            "09:00-10:30",
            "10:40-12:10",
            "12:20-13:50",
            "14:30-16:00",
            "16:10-17:40",
            "17:50-19:20",
            "19:30-21:00"
        ],
        "evening_form": [
            "18:20-19:40",
            "19:50-21:10"
        ]
    }

    def __init__(self, group_name: str, raw_schedule: list = None, date_interval: dict = None) -> None:
        """
        [DESCRIPTION]
            * initializes the Schedule object;

        [ARGS]
            * (required) group_name (str): code-name of the group;
            * (optional) raw_schedule (list of lists): result[0] of API().get_schedule_raw(group_name),
            * - default is None (calls API().get_schedule_raw(group_name));
            * (optional) date_interval (dict): result[1] of API().get_schedule_raw(group_name),
            * - default is None (calls API().get_schedule_raw(group_name));

        [RETURNS]
            * there are no return;

        [ERRORS]
            * ConnectionError() - if there is a problem with the connection;
            * ValueError() - if the schedule is empty or does not exist;
        """

        # getting raw_schedule and date_interval (default is None -> slowly object creation)
        if raw_schedule is None or date_interval is None:
            raw_schedule, date_interval = API().get_schedule_raw(group_name)

        # creating body
        body = []

        # creating day list(s)
        for day in raw_schedule:
            body_day = []
            # creating lesson list(s)
            for lesson in raw_schedule[day]:
                body_lesson = []
                if raw_schedule[day][lesson]:
                    # creating sbj dict(s)
                    for sbj in raw_schedule[day][lesson]:
                        body_sbj = {
                            "name": sbj["sbj"].strip(),
                            "teacher": sbj["teacher"].strip(),
                            "type": sbj["type"].strip(),
                            "location": sbj["location"].strip()
                        }
                        if "df" in sbj:
                            body_sbj["dates"] = {"start": sbj["df"], "finish": sbj["dt"]}
                        else:
                            body_sbj["dates"] = {"start": day, "finish": day}
                        body_lesson.append(body_sbj)
                    body_day.append(body_lesson)
                else:
                    body_day.append([])
            body.append(body_day)

        # filling attributes
        self.body = body
        self.date_interval = date_interval

    @staticmethod
    def __date(date_str: str, date_format: str = "%Y-%m-%d") -> datetime:
        """
        [DESCRIPTION]
            * converts а string to a datetime object, depending on the given format;

        [ARGS]
            * (required) date_str (str): a string with a recorded date;
            * (optional) date_format (str): format of a string with a recorded date,
            * - default is "%Y-%m-%d";

        [RETURNS]
            * date (datetime): datetime object for easy date-manipulation;

        [ERRORS]
            * there are no custom errors;
        """

        # returning datetime object
        return datetime.strptime(date_str, date_format)

    def __check_date(self, d_start: str, d_given: str, d_finish: str) -> bool:
        """
        [DESCRIPTION]
            * checks if the given date is in the given date range;

        [ARGS]
            * (required) d_start (str): start of date range;
            * (required) d_given (str): given date;
            * (required) d_finish (str): finish of date range;

        [RETURNS]
            * flag (bool): True if the given date is in the range, otherwise False;

        [ERRORS]
            * there are no custom errors;
        """

        # returning comparison results
        return self.__date(d_start) <= self.__date(d_given) <= self.__date(d_finish)

    def get_day(self, date_str: str) -> list:
        """
        [DESCRIPTION]
            * returns the schedule of the day for the recorded group;

        [ARGS]
            * (required) date_str (str): a string with a recorded date;

        [RETURNS]
            * day (list of dicts): list for representing academic day ([] if is empty);

        [ERRORS]
            * ValueError() - if the schedule does not exist on the given date;
        """

        # checking the availability of a schedule
        if not self.body:
            return []

        # checking correctness of given date
        if not self.__check_date(self.date_interval["start"], date_str, self.date_interval["finish"]):
            raise ValueError(f"The schedule exists in the interval"
                             f"[{self.date_interval['start']}...{self.date_interval['finish']}], "
                             f"but {date_str} was given.")

        # creating day
        day = []
        if len(self.body) != 0:
            if len(self.body) == 6:
                # 6-day schedule processing
                weekday = self.__date(date_str).weekday()
                if weekday != 6:
                    raw_day = self.body[weekday]
                    for lesson in raw_day:
                        tmp = {}
                        if lesson:
                            for sbj in lesson:
                                if self.__check_date(sbj["dates"]["start"], date_str, sbj["dates"]["finish"]):
                                    tmp = sbj
                                    del tmp["dates"]
                        day.append(tmp)
            else:
                # not 6-day (20, 25) schedule processing
                is_found = False
                tmp = []
                for raw_day in self.body:
                    for lesson in raw_day:
                        if lesson:
                            sbj = lesson[0]
                            if self.__check_date(sbj["dates"]["start"], date_str, sbj["dates"]["finish"]):
                                tmp = raw_day
                                is_found = True
                                break
                    if is_found:
                        break
                for lesson in tmp:
                    if lesson:
                        sbj = lesson[0]
                        day.append({key: sbj[key] for key in sbj if key != "dates"})
                    else:
                        day.append({})

        # returning schedule day representation
        return day


class API:
    """
        [DESCRIPTION]
            * API for working with the services of the Moscow Polytechnic University;
            * https://mospolytech.ru/;

        [ATTRIBUTES]
            * there are no public attributes;

        [ARGS]
            * (optional) user_agent (str): string that lets servers identify the application,
            * - default is __DEFAULT_USER_AGENT;

        [METHODS]
            * get_semester_raw(self) -> dict;
            * get_schedule_raw(self, group: str) -> list;
            * get_group_names(self) -> list;
        """

    # private attributes for API operation
    __URL = "https://rasp.dmami.ru/"
    __DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                           "Chrome/86.0.4240.75 Safari/537.36"

    def __init__(self, user_agent: str = __DEFAULT_USER_AGENT) -> None:
        """
        [DESCRIPTION]
            * initializes the API object;

        [ARGS]
            * (optional) user_agent (str): string that lets servers identify the application,
            * - default is __DEFAULT_USER_AGENT;

        [RETURNS]
            * there are no return;

        [ERRORS]
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
        [DESCRIPTION]
            * checks the correctness of the response status code;

        [ARGS]
            * (required) code (int): response status code;

        [RETURNS]
            * there are no return;

        [ERRORS]
            * ConnectionError() - if there is a problem with the connection;
        """

        # checking status code
        if code != 200:
            raise requests.ConnectionError(f"Expected status code 200, but got {code}.")

    def get_semester_raw(self) -> dict:
        """
        [DESCRIPTION]
            * returns raw data about the current semester for all groups;

        [ARGS]
            * there are no args;

        [RETURNS]
            * semester (dict): a dictionary containing group names and information about its schedule;

        [ERRORS]
            * ConnectionError() - if there is a problem with the connection;
        """

        # making request
        r_url = self.__URL + "semester.json"
        r = requests.get(url=r_url, headers=self.headers)

        # checking status code
        self.__check_status_code(r.status_code)

        # loading content to dict
        data = json.loads(r.content.decode("utf-8"))

        # returning data["contents"] dict
        return data["contents"]

    def get_schedule_raw(self, group_name: str) -> list:
        """
        [DESCRIPTION]
            * returns a raw schedule for the given group and date interval for schedule;

        [ARGS]
            * (required) group_name (str): name of the group;

        [RETURNS]
            * schedule (list of lists): list for representing academic days ([] if is empty);
            * date_interval (dict): dictionary of info about date interval of the given schedule (None if is empty);

        [ERRORS]
            * ConnectionError() - if there is a problem with the connection;
            * ValueError() - if the schedule is empty or does not exist;
        """

        # server messages if there are errors
        NULL_SCHEDULE_CONTENT = "Еще не готово расписание для группы"
        NOT_FOUND_SCHEDULE = "Не нашлось расписание для группы"

        # making request
        r_url = self.__URL + "site/group?group=" + group_name.replace(" ", "%20")
        r = requests.get(url=r_url, headers=self.headers)

        # checking status code
        self.__check_status_code(r.status_code)

        # checking for existence of a schedule
        if r.content.decode("utf-8") == NULL_SCHEDULE_CONTENT:
            raise ValueError(f"The schedule for the '{group_name}' group is empty or does not exist.")

        # loading content to dict
        data = json.loads(r.content)

        # checking the correctness of the information
        if "message" in data:
            if data["message"] == NOT_FOUND_SCHEDULE:
                return [[], None]

        # returning raw schedule list & date interval dict
        return [data["grid"], {"start": data["group"]["dateFrom"], "finish": data["group"]["dateTo"]}]

    def get_group_names(self) -> list:
        """
        [DESCRIPTION]
            * returns a list of group names;

        [ARGS]
            * there are no args;

        [RETURNS]
            * group_names (list of strs): list of group names that are existing;

        [ERRORS]
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
    pass
