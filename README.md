# Mospolytech API

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus porta lacus accumsan, cursus orci a, lobortis dui. Sed ornare vehicula eros vel vulputate. Curabitur ante odio, fermentum sit amet feugiat eget, faucibus in lacus. Vivamus vitae tincidunt arcu, vitae malesuada risus. Quisque sit amet lacinia libero. Ut vitae mauris eu nulla commodo convallis. Vivamus elementum hendrerit lorem eget laoreet. Ut eget dui eget ante ultrices scelerisque. Nullam malesuada a dui eget porta. Aliquam malesuada metus vitae porta tempus. Suspendisse vehicula ligula risus, non posuere nibh mollis nec. Fusce luctus ultrices lacus, eget convallis purus euismod et. In consequat eget justo ut gravida. In augue est, pharetra non tempor vitae, sollicitudin ut nulla. Integer non facilisis dui. Cras vehicula condimentum ex, sit amet molestie risus aliquam in.

## Requirements
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## Features
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## Usage
### API Initialization
```python
from mospolytech_api import api

api = api.API()
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
# students = ["Amy Curtis Laurence", "Elizabeth March", ... "Josephine Bhaer"]

# students of specified  groups
students = api.get_students([
        "201-721", "201-722", "201-723",
        "201-724", "201-725", "201-726"
])
# students = ["Amy Curtis Laurence", "Elizabeth March", ... "Josephine Bhaer"]
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
from mospolytech_api import schedule

schedule_obj = schedule.Schedule(raw_schedule)
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
