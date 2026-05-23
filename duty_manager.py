from utils import find_duty_by_name, find_soldier_by_id, soldeir_had_duty, is_valid_status, is_valid_day


def add_duty_to_soldier(soldier_id: str, duty_name: str, day: str)\
      -> None | ValueError | KeyError:
    """check the new duty if it rully, the func will run a full sets of tests"""

    soldier_data = find_soldier_by_id(soldier_id)

    if not soldier_data:
        raise KeyError(f"soldier id: {soldier_id} doesn't found.")


    if not is_valid_day(day):
        raise ValueError(f"invalid - {day} please enter correct day: sunday - thursday only.")
    

    if soldeir_had_duty(soldier_data ,duty_name):
        raise ValueError(f"invalid - {duty_name}")
    
    new_duty = {"name": duty_name, "day": day, "status": "pending"}
    soldier_data["duties"].append(new_duty)
    return


def update_duty_status(soldier_id: str, duty_name: str, new_status: str) -> None:
        """the runc run test for checking the new status,
          it maigh raise errors if the status is wrong"""
        
        soldier_data = find_soldier_by_id(soldier_id)
        duty_data = find_duty_by_name(soldier_data, duty_name)
        
        if not soldier_data:
            raise KeyError(f"soldier id: {soldier_id} doesn't found.")
        
        if not duty_data:
             raise KeyError(f"duty {duty_name} doesn't found in soldier id {soldier_id}")

        if not is_valid_status(new_status):
             raise ValueError(f"invalid status - {new_status}")
        
        duty_data["status"] = new_status
        return


def get_soldier_duties(soldier_id: str) -> list:
    """return the full soldier's duties by dict"""

    data_soldier = find_soldier_by_id(soldier_id)

    if not data_soldier:
        raise KeyError(f"soldier id: {soldier_id} doesn't found.")
    
    return data_soldier["duties"]
