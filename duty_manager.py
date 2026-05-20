from utils import find_duty_by_name, find_soldier_by_id, soldeir_had_duty, is_valid_status, is_valid_day


def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str)\
      -> None | ValueError | KeyError:
    """check the new duty if it rully, the func will run a full sets of tests"""

    soldier_data = find_soldier_by_id(soldier_id)

    if not soldier_data:
        raise KeyError(f"soldier id: {soldier_id} doesn't found.")


    if not is_valid_day(day):
        raise ValueError(f"invalid - {day} please enter correct day: sunday - thursday only.")
    

    if soldeir_had_duty(duty_name):
        raise ValueError(f"invalid - {duty_name}")
    
    new_duty = {"name": duty_name, "day": day, "status": "pending"}
    soldier_data["duties"].append(new_duty)
    return