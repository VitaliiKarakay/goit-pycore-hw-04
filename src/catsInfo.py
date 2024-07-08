import utils.utils as utils
from utils import constants


def get_cats_info(path):
    lines = utils.read_file_lines(path)
    cats_info = []
    for line in lines:
        try:
            id, name, age = line.strip().split(',')
            cats_info.append({'id': id, 'name': name, 'age': int(age)})
        except ValueError as e:
            print(f"Invalid data: {line} - {e}")

    return cats_info


print(get_cats_info(constants.CATS_FILE_PATH))
