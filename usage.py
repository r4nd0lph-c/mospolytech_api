# Usage examples | version 3.0


import json
from mospolytech_api.api import API
from mospolytech_api.group import Group
from mospolytech_api.schedule import Schedule


if __name__ == "__main__":
    # API initialization
    api = API()

    # getting all available groups
    groups = api.get_groups()
    print(f"\n\nGROUPS:\n{groups}\n\nCOUNT:\n{len(groups)}")

    # getting a sorted list of students from parallel groups
    list_students = api.get_students([
        "201-721", "201-722", "201-723",
        "201-724", "201-725", "201-726"
    ])
    print(f"\n\nSTUDENTS:\n{list_students}\n\nCOUNT:\n{len(list_students)}")

    # getting raw shedule of specified group
    raw_schedule = api.get_schedule("201-721")
    print(f"\n\nSCHEDULE:\n{raw_schedule}")

    # saving raw_schedule to JSON file
    with open("raw_schedule.json", "w", encoding="utf-8") as f:
        json.dump(raw_schedule, f, ensure_ascii=False, indent=4)

    # Group object initialization
    group_obj = Group()

    # ...
    # ...
    # ...

    # Schedule object initialization
    schedule_obj = Schedule(raw_schedule)

    # getting schedule on specified day
    day = schedule_obj.get_day("12.12.2022")
    print(f"\n\nGROUP {schedule_obj.group}, DAY {day['date']}:\n{day['body']}")

    # saving day to JSON file
    with open("day.json", "w", encoding="utf-8") as f:
        json.dump(day, f, ensure_ascii=False, indent=4)
