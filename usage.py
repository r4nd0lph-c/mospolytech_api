# Mospolytech API | Usage examples


import json

from mospolytech_api.api import API
from mospolytech_api.schedule import Schedule


# helper function for saving JSON files
def save(name: str, content: dict) -> None:
    with open(f"{name}.json", "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # api object initialization
    api = API()

    # sorted list of groups
    groups = api.get_groups()
    print(f"GROUPS ({len(groups)}):\n{groups}\n\n")

    # sorted dict of students (all groups)
    students = api.get_students()

    # sorted dict of students (given groups)
    students = api.get_students(
        ["201-721", "201-722", "201-723", "201-724", "201-725", "201-726"]
    )
    save("students", students)

    # semester schedule of all groups
    semester = api.get_semester()
    save("semester", semester)

    # session schedule of all groups
    session = api.get_session()
    save("session", session)

    # schedule for given group
    schedule = api.get_schedule(group="201-721", is_session=False)
    save("schedule", schedule)

    # schedule object initialization
    schedule = Schedule(schedule)

    # schedule of the day
    day = schedule.get_day("01.02.2023")
    save("day", day)

    # schedule of the week
    week = schedule.get_week("01.02.2023")
    save("week", week)
