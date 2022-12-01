from get_most_calories import get_most
from pathlib import Path

def test_get_most_calories():
    assert get_most(Path('Day_1/test_data.txt')) == 4
    print(get_most(Path('Day_1/input.txt')))
