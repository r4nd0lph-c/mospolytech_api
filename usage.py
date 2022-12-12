# Usage examples | version 3.0


import json
from api import mospolytech_api, group, schedule


if __name__ == "__main__":
    # API initialization
    api = mospolytech_api.API()

    # getting all available groups
    list_groups = api.get_groups()
    print(f"\n\nGROUPS:\n{list_groups}\n\nCOUNT:\n{len(list_groups)}")

    # getting a sorted list of students from parallel groups
    list_students = api.get_students([
        "201-721", "201-722", "201-723",
        "201-724", "201-725", "201-726"
    ])
    print(f"\n\nSTUDENTS:\n{list_students}\n\nCOUNT:\n{len(list_students)}")

    # getting the raw shedule of the choosen group
    dict_schedule = api.get_schedule("201-721")
    print(f"\n\nSCHEDULE:\n{dict_schedule}")
