import logging, time

from watchfiles import watch
from cola_deque import ColaDeque

DEBUG = True
level = logging.DEBUG if DEBUG else logging.ERROR
logging.basicConfig(level=level)

STDMAN_FILE = 'archivotest.txt' #file location
ROW_LAST_CHAR = 10      # ROW where is located the last character


def watch_file(path: str, piece_to_mark: ColaDeque):
    logging.info(" Starting watching file %s ", path)
    for changes in watch(path, raise_interrupt=False, rust_timeout= 5000):
        logging.debug(f"   Changes detected on {path}")
        character = get_last_seams(path)
        if character != last_character:
            piece_to_mark.queue(character)
            logging.debug(f"   Character: {character} added to queue")
            last_character = character


def get_last_seams(file_name: str):
    logging.debug("  Starting last_seam")
    target_line = ROW_LAST_CHAR
    try:
        with open(file_name, 'r') as file:
            logging.debug(f" File \"{file_name}\" opened and looking in row {target_line}")
            content = file.readlines()
            last_character = content[target_line - 1]   #index starts in 0
            logging.debug(f" Last character = {last_character}")
            return last_character
    except FileNotFoundError:
        logging.error(" File not founded")
        print("No such file or directory")


if __name__ == '__main__':

