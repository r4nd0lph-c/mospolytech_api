# Mospolytech API

## Description
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus porta lacus accumsan, cursus orci a, lobortis dui. Sed ornare vehicula eros vel vulputate. Curabitur ante odio, fermentum sit amet feugiat eget, faucibus in lacus. Vivamus vitae tincidunt arcu, vitae malesuada risus. Quisque sit amet lacinia libero. Ut vitae mauris eu nulla commodo convallis. Vivamus elementum hendrerit lorem eget laoreet. Ut eget dui eget ante ultrices scelerisque. Nullam malesuada a dui eget porta. Aliquam malesuada metus vitae porta tempus. Suspendisse vehicula ligula risus, non posuere nibh mollis nec. Fusce luctus ultrices lacus, eget convallis purus euismod et. In consequat eget justo ut gravida. In augue est, pharetra non tempor vitae, sollicitudin ut nulla. Integer non facilisis dui. Cras vehicula condimentum ex, sit amet molestie risus aliquam in.

## Requirements
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## Features
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## Usage
```python
import json
from mospolytech_api import api, group, schedule


if __name__ == "__main__":
    # API() initialization
    api = api.API()

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

    # saving the raw schedule to JSON file
    with open("logs_raw_schedule.json", "w", encoding="utf-8") as f:
        json.dump(dict_schedule, f, ensure_ascii=False, indent=4)

    # Group() object initialization
    # group_obj = group.Group()

    # ...
    # ...
    # ...

    # Schedule() object initialization
    schedule_obj = schedule.Schedule(dict_schedule)
    day = schedule_obj.get_day("12.12.2022")
    print(f"\n\nGROUP {schedule_obj.group}, DAY {day['date']}:\n{day['body']}")

```
