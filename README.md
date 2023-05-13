# Mospolytech API

__Mospolytech API__ is an interface that provides Python developers with convenient tools for interacting with the internal services of the [Moscow Polytechnic University](https://mospolytech.ru/en/).

To use the API, download the repository and place it in your project.

```
git clone https://github.com/r4nd0lph-c/mospolytech_api
```

## Requirements

Third-party dependencies are required for the API to work.

```
pip install -r /path/to/requirements.txt
```

List of dependencies:
1. requests==2.28.1

## Features

The following functions are available for use:

- [x] Sorted list of groups
- [x] Sorted dict of students all / given groups
- [x] Semester schedule of all groups
- [x] Session schedule of all groups
- [x] Schedule (general / session) for given group
- [x] Schedule of the day based on raw data
- [x] Schedule of the week based on raw data

## Usage

Code examples for using certain API functions are shown below.

### API object initialization

```python
from mospolytech_api.api import API

api = API()
```

### Getting sorted list of groups

```python
groups = api.get_groups()
# groups = ["181-111", "181-112", "181-113", ..., "22А-531", "22А-811", "22А-812"]
```

### Getting sorted dict of students

Make sure you have the hash salt (written to the file [hash_salt.txt](https://github.com/r4nd0lph-c/mospolytech_api/blob/master/hash_salt.txt) by default).

```python
# all groups
students = api.get_students()

# given groups
students = api.get_students([
    "201-721", "201-722", "201-723",
    "201-724", "201-725", "201-726"
])

# saving students to JSON file
save("students", students)
```

<details> <summary> Check students.json </summary>

```javascript
// students.json

{
    ...,
    "201-721": [
        {
            "guid": "bb85cb84-d7e3-11ea-80b0-fe3e130bd8ea",
            "student": "Amy Curtis Laurence"
        },
        {
            "guid": "8d2ba767-d559-11eb-80d0-fe3e120bd9ea",
            "student": "Elizabeth March"
        },
        {
            "guid": "5e376b82-dba7-12ea-40b0-fe3e120db9ea",
            "student": "Josephine Bhaer"
        },
        ...
    ],
    ...
}
```
</details>

### Getting semester schedule of all groups

```python
semester = api.get_semester()

# saving semester to JSON file
save("semester", semester)
```

<details> <summary> Check semester.json </summary>

```javascript
// semester.json

{
    ...,
    "201-721": {
        "type": "morning",
        "dates": ["30.01.2023", "28.05.2023"],
        "grid": [
            [
                [...],
                [
                    {
                        "title": "Philosophy of life",
                        "type": "Lecture",
                        "teachers": ["Lord Henry Wotton", "Dorian Gray"],
                        "location": "Webinar",
                        "rooms": [],
                        "link": "https://...",
                        "dates": ["24.04.2023", "28.05.2023"]
                    }
                ],
                [
                    {
                        "title": "Art and modern design",
                        "type": "Practice",
                        "teachers": ["Basil Hallward"],
                        "location": "Pryanishnikova",
                        "rooms": ["Pr1429", "Pr1430"],
                        "link": null,
                        "dates": ["24.04.2023", "28.05.2023"]
                    }
                ],
                [...],
                [...],
                [...],
                [...]
            ],
            [...],
            [...],
            [...],
            [...],
            [...],
        ]
    },
    ...
}
```
</details>

### Getting session schedule of all groups

```python
session = api.get_session()

# saving session to JSON file
save("session", session)
```

<details> <summary> Check session.json </summary>

```javascript
// session.json

{
    ...,
    "201-721": {
        "type": "morning",
        "dates": ["26.12.2022", "28.01.2023"],
        "grid": [
            [
                [...],
                [
                    {
                        "title": "Philosophy of life",
                        "type": "Test",
                        "teachers": ["Lord Henry Wotton", "Dorian Gray"],
                        "location": "Webinar",
                        "rooms": [],
                        "link": "https://...",
                        "dates": ["28.01.2023", "28.01.2023"]
                    }
                ],
                [
                    {
                        "title": "Art and modern design",
                        "type": "Exam",
                        "teachers": ["Basil Hallward"],
                        "location": "Pryanishnikova",
                        "rooms": ["Pr2611"],
                        "link": null,
                        "dates": ["28.01.2023", "28.01.2023"]
                    }
                ],
                [...],
                [...],
                [...],
                [...]
            ],
            [...],
            [...],
            [...],
            [...],
            [...],
        ]
    },
    ...
}
```
</details>

### Getting schedule for given group

```python
schedule = api.get_schedule(group="201-721", is_session=False)

# saving schedule to JSON file
save("schedule", schedule)
```

<details> <summary> Check schedule.json </summary>

```javascript
// schedule.json

{
    "group": "201-721",
    "type": "morning",
    "is_session": false,
    "dates": ["30.01.2023", "28.05.2023"],
    "grid": [
        [
            [...],
            [...],
            [
                {
                    "title": "Philosophy of life",
                    "type": "Lecture",
                    "teachers": ["Lord Henry Wotton", "Dorian Gray"],
                    "location": "Webinar",
                    "rooms": [],
                    "link": "https://...",
                    "dates": ["24.04.2023", "28.05.2023"]
                },
                {
                    "title": "Art and modern design",
                    "type": "Practice",
                    "teachers": ["Basil Hallward"],
                    "location": "Pryanishnikova",
                    "rooms": ["Pr1429", "Pr1430"],
                    "link": null,
                    "dates": ["24.04.2023", "28.05.2023"]
                }
            ],
            [...],
            [...],
            [...],
            [...]
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

schedule = Schedule(schedule)
```

### Getting schedule of the day

```python
day = schedule.get_day("01.02.2023")

# saving day to JSON file
save("day", day)
```

<details> <summary> Check day.json </summary>

```javascript
// day.json
{
    "group": "201-721",
    "type": "morning",
    "is_session": false,
    "date": "01.02.2023",
    "day": [
        {
            "time": ["09:00", "10:30"],
            "subject": null
        },
        {
            "time": ["10:40", "12:10"],
            "subject": {
                "title": "Philosophy of life",
                "type": "Lecture",
                "teachers": ["Lord Henry Wotton", "Dorian Gray"],
                "location": "Webinar",
                "rooms": [],
                "link": "https://...",
                "dates": ["24.04.2023", "28.05.2023"]
            }
        },
        {
            "time": ["12:20", "13:50"],
            "subject": null
        },
        {
            "time": ["14:30", "16:00"],
            "subject": {
                "title": "Art and modern design",
                "type": "Practice",
                "teachers": ["Basil Hallward"],
                "location": "Pryanishnikova",
                "rooms": ["Pr1429", "Pr1430"],
                "link": null,
                "dates": ["24.04.2023", "28.05.2023"]
            }
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

### Getting schedule of the week

```python
week = schedule.get_week("01.02.2023")

# saving week to JSON file
save("week", week)
```

<details> <summary> Check week.json </summary>

```javascript
// week.json

{
    "group": "201-721",
    "type": "morning",
    "is_session": false,
    "dates": ["30.01.2023", "05.02.2023"],
    "week": [
    {...},
    {...},
    {
        "date": "01.02.2023",
        "day": [
            {
                "time": ["09:00", "10:30"],
                "subject": null
            },
            {
                "time": ["10:40", "12:10"],
                "subject": {
                    "title": "Philosophy of life",
                    "type": "Lecture",
                    "teachers": ["Lord Henry Wotton", "Dorian Gray"],
                    "location": "Webinar",
                    "rooms": [],
                    "link": "https://...",
                    "dates": ["24.04.2023", "28.05.2023"]
                }
            },
            {
                "time": ["12:20", "13:50"],
                "subject": null
            },
            {
                "time": ["14:30", "16:00"],
                "subject": {
                    "title": "Art and modern design",
                    "type": "Practice",
                    "teachers": ["Basil Hallward"],
                    "location": "Pryanishnikova",
                    "rooms": ["Pr1429", "Pr1430"],
                    "link": null,
                    "dates": ["24.04.2023", "28.05.2023"]
                }
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
    },
    {...},
    {...},
    {...},
    {...}
    ]
}
```
</details>

### More examples

Examples of using all available functionality are in the file [usage.py](usage.py).

## Contacts

If you want to help with development or if you have questions, you can contact the repository creator ([@rand0lphc](https://t.me/rand0lphc)) in telegram.
