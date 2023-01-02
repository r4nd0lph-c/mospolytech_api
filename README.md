# Mospolytech API

__Mospolytech API__ is an interface that provides Python developers with convenient tools for interacting with the internal services of the [Moscow Polytechnic University](https://mospolytech.ru/en/).

To use the API, download the repository and place it in your project.

## Requirements

Third-party dependencies are required for the API to work. How to install it is shown below.

```
pip install -r /path/to/requirements.txt
```

List of dependencies:
1. requests==2.28.1

## Features

The project is in development. But certain functions can already be used (they are checked in the list).

- [x] Getting a list of studying groups
- [ ] Getting information about the group based on the code name
- [x] Getting a list of students for the given groups
- [ ] Getting information about a particular student's visit to a university
- [x] Getting the group schedule in raw form
- [x] Getting the current group schedule based on raw data

## Usage

Code examples for using certain API functions are shown below.

### API Initialization

```python
from mospolytech_api.api import API

api = API()
```

###  Getting available groups

``` python
groups = api.get_groups()
# groups = ["181-111", "181-112", "181-113", ..., "22А-531", "22А-811", "22А-812"]
```

###  Getting list of students

``` python
# students of all  groups
students = api.get_students()
# students = ["Amy Curtis Laurence", "Elizabeth March", ..., "Josephine Bhaer"]

# students of specified  groups
students = api.get_students([
    "201-721", "201-722", "201-723",
    "201-724", "201-725", "201-726"
])
# students = ["Amy Curtis Laurence", "Elizabeth March", ..., "Josephine Bhaer"]
```

### Getting raw shedule of specified group

```python
raw_schedule = api.get_schedule("201-721")

# saving raw_schedule to JSON file
with open("raw_schedule.json", "w", encoding="utf-8") as f:
    json.dump(raw_schedule, f, ensure_ascii=False, indent=4)
```

<details><summary>Check raw_schedule.json</summary>

```javascript
// raw_schedule.json
{
    "group": "201-721",
    "type": "morning",
    "dates": ["01.09.2022", "25.12.2022"],
    "grid": [
        [
            {
                "subjects": [
                    {
                        "title": "Philosophy of life",
                        "type": "Lecture",
                        "teachers": ["Lord Henry Wotton", "Dorian Gray"],
                        "location": "Webinar",
                        "rooms": [],
                        "dates": ["01.09.2022", "30.10.2022"]
                    },
                    {
                        "title": "Art and modern design",
                        "type": "Practice",
                        "teachers": ["Basil Hallward"],
                        "location": "Pryanishnikova",
                        "rooms": ["Pr1429", "Pr1430"],
                        "dates": ["31.10.2022", "25.12.2022"]
                    }
                ]
            },
            {
                "subjects": []
            },
            {...},
            {...},
            {...},
            {...},
            {...}
        ],
        [...],
        [...],
        [...],
        [...],
        [...]
    ]
}
```
</details>

### Schedule object initialization

```python
from mospolytech_api.schedule import Schedule

schedule_obj = Schedule(raw_schedule)
```

### Getting schedule on specified day

```python
day = schedule_obj.get_day("12.12.2022")

# saving day to JSON file
with open("day.json", "w", encoding="utf-8") as f:
    json.dump(day, f, ensure_ascii=False, indent=4)
```

<details><summary>Check day.json</summary>

```javascript
// day.json
{
    "date": "12.12.2022",
    "body": [
        {
            "time": ["09:00", "10:30"],
            "subject": {
                "title": "Art and modern design",
                "type": "Practice",
                "teachers": ["Basil Hallward"],
                "location": "Pryanishnikova",
                "rooms": ["Pr1429", "Pr1430"]
            }
        },
        {
            "time": ["10:40", "12:10"],
            "subject": null
        },
        {
            "time": ["12:20", "13:50"],
            "subject": null
        },
        {
            "time": ["14:30", "16:00"],
            "subject": null
        },
        {
            "time": ["16:10", "17:40"],
            "subject": null
        },
        {
            "time": ["17:50", "19:20"],
            "subject": null
        },
        {
            "time": ["19:30", "21:00"],
            "subject": null
        }
    ]
}
```
</details>

### More examples

Examples of using all available functionality are in the file [usage.py](usage.py).

## Contacts

If necessary, use telegram ([@rand0lphc](https://t.me/rand0lphc)) to contact the repository creator.