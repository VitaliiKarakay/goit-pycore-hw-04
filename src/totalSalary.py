import utils.utils as utils
from utils import constants


def process_line(line):
    try:
        name, salary = line.strip().split(',')
        return int(salary)
    except ValueError as e:
        print(f"Invalid data: {line} - {e}")
        return 0


def total_salary(path):
    lines = utils.read_file_lines(path)
    salary_sum = 0
    count = 0
    for line in lines:
        salary = process_line(line)
        if salary != 0:
            salary_sum += salary
            count += 1

    if count == 0:
        return 0, 0
    return salary_sum, salary_sum / count


total, average = total_salary(constants.SALARY_FILE_PATH)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
