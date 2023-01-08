# Usage examples | version 1.4


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

    # getting a global semester schedule
    semester_schedule = api.get_semester()
    print(f"\n\nSEMESTER:\n{semester_schedule}")

    # saving global semester schedule to JSON file
    with open("semester_schedule.json", "w", encoding="utf-8") as f:
        json.dump(semester_schedule, f, ensure_ascii=False, indent=4)

    # getting a global session schedule
    session_schedule = api.get_session()
    print(f"\n\nSESSION:\n{session_schedule}")

    # saving global session schedule to JSON file
    with open("session_schedule.json", "w", encoding="utf-8") as f:
        json.dump(session_schedule, f, ensure_ascii=False, indent=4)

    try:
        # getting raw shedule (semester) of specified group
        raw_schedule = api.get_schedule("201-721")
        print(f"\n\nSEMESTER SCHEDULE:\n{raw_schedule}")

        # saving raw_schedule to JSON file
        with open("raw_schedule_semester.json", "w", encoding="utf-8") as f:
            json.dump(raw_schedule, f, ensure_ascii=False, indent=4)
    except ValueError as e:
        print(e.args)

    try:
        # getting raw shedule (session) of specified group
        raw_schedule = api.get_schedule("201-721", is_session=True)
        print(f"\n\nSESSION SCHEDULE:\n{raw_schedule}")

        # saving raw_schedule to JSON file
        with open("raw_schedule_session.json", "w", encoding="utf-8") as f:
            json.dump(raw_schedule, f, ensure_ascii=False, indent=4)
    except ValueError as e:
        print(e.args)

    # Group object initialization
    group_obj = Group()

    # ...
    # ...
    # ...

    # getting raw shedule (session) of specified group
    raw_schedule = api.get_schedule("201-721", is_session=True)

    # Schedule object initialization
    schedule_obj = Schedule(raw_schedule)

    # getting schedule on specified day
    day = schedule_obj.get_day("09.01.2023")
    print(f"\n\nGROUP {schedule_obj.group}, DAY {day['date']}:\n{day['body']}")

    # saving day to JSON file
    with open("day.json", "w", encoding="utf-8") as f:
        json.dump(day, f, ensure_ascii=False, indent=4)
