import datetime

custom_reflections = {
    "ena": "inti",
    "ena kont": "inti kont",
    "ena howa": "inti howa",
    "ena n7eb": "inti t7eb",
    "mte3i": "mte3ek",
    "taw na3mel": "taw ta3mel",
    "ena 3andi": "inti 3andek"
}

ayamet_data = {
    'Monday': ' thnin',
    'Tuesday': 'Tletha',
    'Wednesday': ' erb3a',
    'Thursday': ' 5mis',
    'Friday': ' jem3a',
    'Saturday': ' sebt',
    'Sunday': 'a7ad'
}

time_data = {
    'hour': {
        '00': 'nos lil',
        '01': 'madis3a mte3 lil',
        '02': 'madise3tin mte3 lil',
        '03': 'maditletha mte3 lil',
        '04': 'larb3a mte3 sbe7',
        '05': '5amsa mte3 sbe7',
        '06': 'seta mte3 sbe7',
        '07': 'sab3a mte3 sbe7',
        '08': 'thmanya mte3 sbe7',
        '09': 'tes3a mte3 sbe7',
        '10': '3achra mte3 sbe7',
        '11': 'la7dech',
        '12': 'nos nhar',
        '13': 'madis3a ',
        '14': 'madise3tin',
        '15': 'maditletha',
        '16': 'larb3a mte3 3cheya',
        '17': '5amsa mte3 3cheya',
        '18': 'seta mte3 3cheya',
        '19': 'sab3a mte3 lil',
        '20': 'thmanya mte3 lil',
        '21': 'tes3a mte3 lil',
        '22': '3achra mte3 lil',
        '23': 'la7dech mte3 lil'
    }
}

def whichDay(ch: str) -> str:
    return ayamet_data[ch]

def whichTime(ch: str) -> str:
    a: list[str] = ch.split(':')
    return str(time_data['hour'][a[0]])+ ' w ' + a[1] + ' d9i9a'

