import utils
import data


def add_soldier(soldier_id: str, soldier_name: str) -> None |ValueError:
    """calls other function for check validilation and creates a new dict in data"""

    if utils.find_soldier_by_id(soldier_id):
        raise ValueError("soldier alrady exist.")
    
    if not utils.is_valid_name(soldier_name):
        raise ValueError("empty name, name must be not empty.")
    data_dict = {"id": soldier_id, 
                 "nane": soldier_name,
                 "duties": []
                 }
    data.soldiers.append(data_dict)


def remove_soldier(soldier_id: str) -> None | KeyError:
    """remove the soldier's dict from the data,
      if the id doesn't found, a value error will raise"""
    
    soldier_for_remove = utils.find_soldier_by_id(soldier_id)
    
    if soldier_for_remove is None:
        raise KeyError("soldier id doesn't found.")
    
    data.soldiers.remove(soldier_for_remove)


def get_all_soldiers():
    """present list of all the soldiers dictionary"""

    return data.soldiers