import os
import shutil
from zipfile import ZipFile


def main() -> None:
    pass


if __name__ == "__main__":
    main()


def rename_files_and_move(parent_directory: str, new_directory: str) -> None:
    for folder in os.listdir(parent_directory):
        full_folder: str = os.path.join(parent_directory, folder)

        if not os.path.isdir(full_folder):
            continue

        for file in os.listdir(full_folder):

            if file.endswith(".bin"):
                src_file_path: str = os.path.join(full_folder, file)
                zip_name: str = file.replace(".bin", ".zip")
                zip_path: str = os.path.join(full_folder, zip_name)

                shutil.copy(src_file_path, zip_path)
                unzip_and_move(zip_path, new_directory)


def unzip_and_move(zip_path: str, new_directory: str) -> None:
    with ZipFile(zip_path, "r") as zObject:
        zObject.extractall(new_directory)
        os.remove(zip_path)
