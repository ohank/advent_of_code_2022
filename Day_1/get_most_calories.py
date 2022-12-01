from pathlib import Path

def get_most(data_file: Path)-> int:
    with open(data_file, 'r') as f:
        lines = f.read()
    elf_sum: dict = {}
    elf_collection = lines.split('\n\n')
    elf_collection = [i.split('\n') for i in elf_collection]
    elf_collection = [[int(y) for y in i] for i in elf_collection]
    for number, calories in enumerate(elf_collection):
        elf_sum[number+1] = sum(calories)
    return max(elf_sum, key=elf_sum.get)