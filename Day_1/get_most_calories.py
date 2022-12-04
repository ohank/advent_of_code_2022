from pathlib import Path
from typing import List
def convert_data_to_int(str_list: List[List[str]]) -> List[List[int]]:
        return [[int(y) for y in i] for i in str_list]
def loade_input_file(data_file) -> List[List[int]]:
    with open(data_file, 'r') as f:
        lines = f.read()

    unit_collection = lines.split('\n\n')
    unit_collection = [i.split('\n') for i in unit_collection]
    unit_collection = convert_data_to_int(unit_collection)
    return unit_collection

def calculate_calories(data_file: Path)-> List[int]:

    calories_sum: list = []
    calories_collection = loade_input_file(data_file=data_file)
    for number, calories in enumerate(calories_collection):
        calories_sum.append(sum(calories))
    calories_sum.sort()
    return calories_sum

def get_most(units_to_get: int, data_file: Path) -> List[int]:
    calories_list = calculate_calories(data_file=data_file)
    calories_list.reverse()
    return calories_list[0:units_to_get]