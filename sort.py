
def normalize(file: str) -> str: #змінює назву файлу




    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ?<>,!@#[]#$%^&*()-=; "
    LAT_SYMBOLS = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t",
               "u","f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_", "_" ,
               "_", "_", "_", "_","_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_")
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, LAT_SYMBOLS):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    return file.translate(TRANS)


#############
import json
import shutil
import json
import shutil
import sys
from pathlib import Path


def main():  # перевірка на входження аргументу ПРАЦЮЄ!!!

    path = None
    try:
        path = Path(sys.argv[1])
    except IndexError:
        print("Type path to folder")
    if not path.exists():
        print("Folder is not exist. Try again.")
    return path


def delete_folder(path: Path):  # видалення порожніх папок

    if path.stat().st_size == 0:
        path.rmdir()


def normalize(file: str) -> str:  # змінює назву файлу

    # змінює назву у консолі якщо принтити але вайли у папці залишаються без змін

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ?<>,!@#[]#$%^&*()-=; "
    LAT_SYMBOLS = (
        "a",
        "b",
        "v",
        "g",
        "d",
        "e",
        "e",
        "j",
        "z",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "r",
        "s",
        "t",
        "u",
        "f",
        "h",
        "ts",
        "ch",
        "sh",
        "sch",
        "",
        "y",
        "",
        "e",
        "yu",
        "ya",
        "je",
        "i",
        "ji",
        "g",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
        "_",
    )
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, LAT_SYMBOLS):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()


    return file.translate(TRANS)


def create_categories(path):  # створення категорій на підставі файлу json ПРАЦЮЄ!!!
    # Тут буде трошки не так. файл з категоріями у Вас буде завжди в теці зі скриптом, тому потрібно використати відносний шлях
    with open(path) as f:
        result = json.load(f)
    return result


def archive(archive_path: Path, current_path: Path):  # розпакування архиву
    shutil.unpack_archive(
        archive_path, current_path.joinpath("archives", archive_path.stem)
    )




def create_folder_cat(path: Path, file_path: Path):  # створення папок для сортування ПРАЦЮЄ!!! path==work_dir
    CATEGORIES = create_categories("cat.json")
    new_path = None
    for suff in CATEGORIES:
        if file_path.suffix.lower() in CATEGORIES[suff]:
            if not path.joinpath(suff).exists():
                path.joinpath(suff).mkdir()
            new_path = file_path.replace(
                path.joinpath(suff, f"{normalize(file_path.stem)}{file_path.suffix}")     #replace - перезаписівает путь файла в новой папке
            )
            if file_path.suffix in CATEGORIES["archives"]:
                archive(new_path, path)


def sort_file():

    work_dir = Path(main())
    # CATEGORIES = create_categories('cat.json')
    for file in work_dir.glob("**/*"):
        # if file.is_dir():
        #     delete_folder(file)
        create_folder_cat(work_dir, file)


if __name__ == "__main__":

    # main()
    sort_file()
