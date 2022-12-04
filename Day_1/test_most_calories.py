from get_most_calories import get_most
from pathlib import Path
import os

def test_get_most_calories():
    assert get_most(units_to_get=1, data_file=Path(os.path.join('advent_of_code_2022\Day_1', 'test_data.txt')))[0] == 24000

def test_get_calories_top_tre():
    assert get_most(units_to_get=3, data_file=Path(os.path.join('advent_of_code_2022\Day_1', 'test_data.txt'))) == [24000, 11000, 6000]

def test_sum_tre_most():
    tre_most = get_most(units_to_get=3, data_file=Path(os.path.join('advent_of_code_2022\Day_1', 'input2.txt')))
    assert sum(tre_most) == 208437
