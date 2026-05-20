import utils
import data


def add_soldier(soldier_id: int, soldier_name: str) -> None |ValueError:
    """calls other function for check validilation and creates a new dict in data"""

    if utils.find_soldier_by_id(soldier_id):
        raise ValueError
    
    if not utils.is_valid_name(soldier_name):
        raise ValueError
    data_dict = {"id": soldier_id, 
                 "nane": soldier_name,
                 "duties": []
                 }
    data.soldiers.append(data_dict)