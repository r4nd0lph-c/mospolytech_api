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
list_groups = api.get_groups()
# list_groups = ["181-111", "181-112", "181-113", ..., "22А-531", "22А-811", "22А-812"]
```


###  Getting list of students
``` python
# students of all  groups
list_students = api.get_students()
# list_students = ["Abbie Choi", "Alan Trevino", ... "Zion Andrews"]

# students of specified  groups
list_students = api.get_students([
        "201-721", "201-722", "201-723",
        "201-724", "201-725", "201-726"
    ])
# list_students = ["Abbie Choi", "Alan Trevino", ... "Zion Andrews"]
```

### Getting raw shedule of specified group
```python
    dict_schedule = api.get_schedule("201-721")
    
    # saving raw schedule to JSON file
    with open("raw_schedule.json", "w", encoding="utf-8") as f:
        json.dump(dict_schedule, f, ensure_ascii=False, indent=4)
```

```javascript
// raw_schedule.json
{
    "group": "201-721",
    "type": "morning",
    "dates": [
        "01.09.2022",
        "25.12.2022"
    ],
    "grid": [
        [
            {
                "subjects": [
                    {
                        "title": "Information systems tools",
                        "type": "Lecture",
                        "teachers": [
                            "Randolph Carter",
                            "Dorian Gray"
                        ],
                        "location": "Webinar",
                        "rooms": [],
                        "dates": [
                            "01.09.2022",
                            "30.10.2022"
                        ]
                    },
                    {
                        "title": "Programming for mobile devices",
                        "type": "Practice",
                        "teachers": [
                            "Orlando Jacobson"
                        ],
                        "location": "Pryanishnikova",
                        "rooms": [
                            "Pr1429",
                            "Pr1430"
                        ],
                        "dates": [
                            "31.10.2022",
                            "25.12.2022"
                        ]
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
