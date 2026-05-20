import data


def is_valid_name(name: str) -> bool:
    """the value must to be not empty"""

    return bool(name)


def soldeir_had_duty(soldier: dict, duty_name: str) -> bool:
    """checking if the duty name olrady exist in duties, duty can't appear more than once"""

    for duty in soldier["duties"]:
        duty: dict
        if duty["name"] == duty_name:
            return True
    return False


def is_valid_day(day: str) -> bool:
    """the runction checks is the day is friday or saturday, the soldier can't do the duty on these days"""

    valid_days = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
    return day.lower() in valid_days


def find_soldier_by_id(soldier_id: int) -> None | dict:
    """looking up for soldier in all the dict data,
      if the soldier alrady inside, return dict with the ditails of the soldier """
    
    for soldier in data.soldiers:
        if soldier["soldier_id"] == soldier_id:
            return soldier
    
