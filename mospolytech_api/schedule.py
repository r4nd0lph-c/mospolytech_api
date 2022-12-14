# --------------------------------------------------------------------------------------------------------------------#
# ███╗   ███╗ ██████╗ ███████╗██████╗  ██████╗ ██╗  ██╗   ██╗████████╗███████╗ ██████╗██╗  ██╗     █████╗ ██████╗ ██╗ #
# ████╗ ████║██╔═══██╗██╔════╝██╔══██╗██╔═══██╗██║  ╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔══██╗██║ #
# ██╔████╔██║██║   ██║███████╗██████╔╝██║   ██║██║   ╚████╔╝    ██║   █████╗  ██║     ███████║    ███████║██████╔╝██║ #
# ██║╚██╔╝██║██║   ██║╚════██║██╔═══╝ ██║   ██║██║    ╚██╔╝     ██║   ██╔══╝  ██║     ██╔══██║    ██╔══██║██╔═══╝ ██║ #
# ██║ ╚═╝ ██║╚██████╔╝███████║██║     ╚██████╔╝███████╗██║      ██║   ███████╗╚██████╗██║  ██║    ██║  ██║██║     ██║ #
# ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚══════╝╚═╝      ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝ #
# author: https://t.me/rand0lphc                                                                          version 1.4 #
# ------------------------------------------------------------------------------------------------------------------- #


from datetime import datetime


class Schedule:
    """
    DESCRIPTION
        * a class representing a schedule of a group;
        * contains information about the schedule;

    ATTRIBUTES
        * TIME_SECTIONS (dict): time sections for different forms of education;
        * group (str): name of the group;
        * type (str): type of the group;
        * dates (list[str]): range of available dates;

    ARGS
        * (required) raw_schedule (dict): dict containing raw schedule information;

    METHODS
        * get_day(date: str) -> dict;
    """

    TIME_SECTIONS = {
        "morning": [
            ["09:00", "10:30"],
            ["10:40", "12:10"],
            ["12:20", "13:50"],
            ["14:30", "16:00"],
            ["16:10", "17:40"],
            ["17:50", "19:20"],
            ["19:30", "21:00"]
        ],
        "evening": [
            ["09:00", "10:30"],
            ["10:40", "12:10"],
            ["12:20", "13:50"],
            ["14:30", "16:00"],
            ["16:10", "17:40"],
            ["18:20", "19:40"],
            ["19:50", "21:10"]
        ]
    }

    def __init__(self, raw_schedule: dict) -> None:
        """
        DESCRIPTION
            * initializes the Schedule object;

        ARGS
            * (required) raw_schedule (dict): dict containing raw schedule information;

        RETURNS
            * there are no return;

        ERRORS
            * there are no custom errors;
        """

        self.group = raw_schedule["group"]
        self.type = raw_schedule["type"]
        self.dates = raw_schedule["dates"]
        self.__grid = raw_schedule["grid"]

    @staticmethod
    def __d(date: str, format: str = "%d.%m.%Y") -> datetime:
        """
        DESCRIPTION
            * converts a date string to a datetime object, depending on the given format;

        ARGS
            * (required) date (str): a string with a recorded date;
            * (optional) format (str): format of a string with a recorded date,
            * default is "%d.%m.%Y";

        RETURNS
            * date (datetime): datetime object for easy date-manipulation;

        ERRORS
            * there are no custom errors;
        """

        # returning datetime object
        return datetime.strptime(date, format)

    def get_day(self, date: str) -> dict:
        """
        DESCRIPTION
            * returns a dict with information about the study day;

        ARGS
            * (required) date (str): date of the day (format: "%d.%m.%Y");

        RETURNS
            * day (dict): a dict containing the date and pairs of the study day;

        ERRORS
            * ValueError(): if there is a problem with the range of available dates;
        """

        # checking correctness of date
        if not (self.__d(self.dates[0]) <= self.__d(date) <= self.__d(self.dates[1])):
            raise ValueError(
                f"The specified date {date} is outside the range of available dates: [{self.dates[0]} - {self.dates[1]}]."
            )

        # creating day
        day = {
            "date": date,
            "body": []
        }

        # getting raw body
        if len(self.__grid) == 6:
            # first case (per-week schedule)
            w = self.__d(date).weekday()
            raw_body = self.__grid[w]
        else:
            # second case (per-day schedule)
            d = abs((self.__d(date) - self.__d(self.dates[0])).days)
            raw_body = self.__grid[d]

        # filling body
        for index, pair in enumerate(raw_body):
            sbj = {
                "time": self.TIME_SECTIONS[self.type][index],
                "subject": None
            }
            for raw_sbj in pair["subjects"]:
                if self.__d(raw_sbj["dates"][0]) <= self.__d(date) <= self.__d(raw_sbj["dates"][1]):
                    del raw_sbj["dates"]
                    sbj["subject"] = raw_sbj
                    break
            day["body"].append(sbj)

        # returning day
        return day


if __name__ == "__main__":
    pass
