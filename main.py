import os
from zipfile import ZipFile


def main() -> None:
    pass


if __name__ == "__main__":
    main()


def unzip_and_move(zip_path: str, new_directory: str) -> None:
    with ZipFile(zip_path, "r") as zObject:
        zObject.extractall(new_directory)
        os.remove(zip_path)
