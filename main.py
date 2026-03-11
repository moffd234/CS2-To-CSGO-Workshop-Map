import os
import shutil
import time
from argparse import ArgumentParser, Namespace
from zipfile import ZipFile

STEAM_APPS_DIRECTORY = r""
DEFAULT_CS2_DIRECTORY = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\730"
DEFAULT_CSGO_DIRECTORY = r"C:\Program Files (x86)\Steam\steamapps\common\csgo legacy\csgo\maps"


def unzip_and_move(zip_path: str, new_directory: str) -> None:
    try:
        with ZipFile(zip_path, "r") as zObject:
            zObject.extractall(new_directory)
            print(f"Extracted {zip_path}")
    except PermissionError:
        print(f"Error extracting zip file at {zip_path}. Check if the file is in use")

    finally:
        try:
            os.remove(zip_path)
        except PermissionError:
            print(f"***Error*** \n error deleting zip file at {zip_path}")



def rename_files_and_move(parent_directory: str, dst_directory: str) -> None:
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
                unzip_and_move(zip_path, dst_directory)


def main() -> None:
    parent_directory: str = DEFAULT_CS2_DIRECTORY
    dst_directory: str = DEFAULT_CSGO_DIRECTORY

    parser: ArgumentParser = ArgumentParser(description="Flag parser")
    parser.add_argument("-s", "--src", help="Source folder (CS2 folder)", required=False, default=DEFAULT_CS2_DIRECTORY)
    parser.add_argument("-d", "--dst", help="Destination folder (CSGO folder)", required=False,
                        default=DEFAULT_CSGO_DIRECTORY)

    arguments: Namespace = parser.parse_args()

    if arguments.src:
        parent_directory = arguments.src

    if arguments.dst:
        dst_directory = arguments.dst

    if not os.path.exists(parent_directory):
        print("ERROR: Source directory (CS2 directory) does not exist. Exiting")
        input("Press enter to exit")
        return

    if not os.path.exists(dst_directory):
        print("ERROR: Destination directory (CSGO Legacy maps directory) does not exist. Exiting")
        input("Press enter to exit")
        return

    rename_files_and_move(parent_directory, dst_directory)
    print("Finished moving maps...")
    input("Press enter to exit")


if __name__ == "__main__":
    main()
