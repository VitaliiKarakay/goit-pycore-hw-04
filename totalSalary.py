from pathlib import Path
import constants

path = Path(constants.SALARY_FILE_PATH)


def read_file_lines(path):
    try:
        with path.open('r') as file:
            return file.readlines()
    except (FileNotFoundError, OSError) as e:
        print(f"Error opening file: {e}")

        return []


def process_line(line):
    try:
        name, salary = line.strip().split(',')
        return int(salary)
    except ValueError as e:
        print(f"Invalid data: {line} - {e}")
        return 0


def total_salary(path):
    lines = read_file_lines(path)
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


print(total_salary(path))
