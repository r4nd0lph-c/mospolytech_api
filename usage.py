# Mospolytech API | Usage examples


import json

from mospolytech_api.api import API
from mospolytech_api.group import Group
from mospolytech_api.schedule import Schedule


if __name__ == "__main__":
    # api object initialization
    api = API()

    # sorted list of groups
    groups = api.get_groups()
    # printing sorted list of groups
    print(f"GROUPS ({len(groups)}):\n{groups}\n\n")

    # group object initialization
    group = Group()
    # TODO: logic...

    # sorted list of students (all groups)
    students = api.get_students()
    # printing sorted list of students
    print(f"STUDENTS ({len(students)}):\n{students}\n\n")

    # sorted list of students (given groups)
    students = api.get_students(
        ["201-721", "201-722", "201-723", "201-724", "201-725", "201-726"]
    )
    # printing sorted list of students
    print(f"STUDENTS ({len(students)}):\n{students}\n\n")

    # semester schedule of all groups
    semester = api.get_semester()
    # saving semester to JSON file
    with open("semester.json", "w", encoding="utf-8") as f:
        json.dump(semester, f, ensure_ascii=False, indent=4)

    # session schedule of all groups
    session = api.get_session()
    # saving session to JSON file
    with open("session.json", "w", encoding="utf-8") as f:
        json.dump(session, f, ensure_ascii=False, indent=4)

    # schedule for given group
    schedule = api.get_schedule(group="201-721", is_session=False)
    # saving schedule to JSON file
    with open("schedule.json", "w", encoding="utf-8") as f:
        json.dump(schedule, f, ensure_ascii=False, indent=4)

    # schedule object initialization
    schedule = Schedule(schedule)

    # schedule of the day
    day = schedule.get_day("01.02.2023")
    # saving day to JSON file
    with open("day.json", "w", encoding="utf-8") as f:
        json.dump(day, f, ensure_ascii=False, indent=4)

    # schedule of the week
    week = schedule.get_week("01.02.2023")
    # saving week to JSON file
    with open("week.json", "w", encoding="utf-8") as f:
        json.dump(week, f, ensure_ascii=False, indent=4)
