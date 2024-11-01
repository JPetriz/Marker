import logging, time

from watchfiles import watch

DEBUG = True
level = logging.DEBUG if DEBUG else logging.ERROR
logging.basicConfig(level=level)


def watch_file(path: str):
    for changes in watch(path, raise_interrupt=False, rust_timeout= 5000):
        print(changes)
        print("hubo cambvios")

def last_seam(file_name: str, target_line: int):
    try:
        with open(file_name, 'r') as file:
            logging.debug(f" File \"{file_name}\" founded")
            content = file.readlines()
            seam_cycle = content[target_line - 1]
            return seam_cycle
    except FileNotFoundError:
        logging.error(" File not founded")
        print("No such file or directory")

if __name__ == '__main__':
    #print(last_seam('archivotest.txt', 10))
    watch_file("archivotest.txt")
