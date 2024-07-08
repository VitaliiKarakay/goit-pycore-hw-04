from pathlib import Path


def read_file_lines(path):
    path = Path(path)
    try:
        with path.open('r') as file:
            return file.readlines()
    except (FileNotFoundError, OSError) as e:
        print(f"Error opening file: {e}")

        return []
