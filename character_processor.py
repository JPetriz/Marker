import logging, firebirdsql

from cola_deque import ColaDeque
from register import Register
from trailer_hitch import TrailerHitch

DEBUG = True
level = logging.DEBUG if DEBUG else logging.ERROR
logging.basicConfig(level=level)

HOST = "localhost"
DATABASE = "D:/weldQAS/Data/WELDDB60.GBD"
USER = "SYSDBA"
PASSWORD = "masterkey"

serie = -1


def get_registers(character: str) -> Register:
    """
    This function consults the HKS database, search for all the seams with the same character and return them
in a register list object

    :param character:
    :return Register:
    """
    logging.info(f"   Accessing Data Base")
    try:
        # establish connection to database
        conn = firebirdsql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        # create a cursor
        cursor = conn.cursor()

        # Get the quantity of seams there are with the DESCRIPTION0 = character
        query = f"SELECT COUNT(DESCRIPTION0) FROM RESULT WHERE (DESCRIPTION0 = '{character}') AND (MARKMAX > 0.0)"

        logging.debug(f"  Executing query: {query}")

        #run query
        cursor.execute(query)
        #get the quantity of seams
        count = cursor.fetchone()
        logging.debug(f"   Result from query: {count}")
        if count > 0:
            # create 'count' numbers of registers
            registers = [Register() for x in range(count)]
            """
            DESCRIPTION0    --->    Character
            TECHIDENTNO     --->    Program number
            MARKMAX         --->    Score
            REGISTRATIONDATETIME    --->    Date
            MCVALUE1        --->    Voltage
            MCVALUE2        --->    Gas
            MCVALUE3        --->    Wire
            """
            # Get all the register values with the DESCRIPTION0 = character
            query = f"""SELECT DESCRIPTION0, TECHINDENTNO, MARKMAX, REGISTRATIONDATETIME, MCVALUE1, MCVALUE2, MCVALUE3
            FROM RESULT WHERE (DESCRIPTION0 = '{character}') AND (MARKMAX > 0.0) ORDER BY TECHINDENTNO ASC"""

            logging.debug(f"  Executing query: {query}")

            # run query
            cursor.execute(query)
            result = cursor.fetchall()
            logging.debug(f"   Result from query: {result}")
            for row in result:
                #result[row][0] = key
                #result[row][1] =  character
                program_number = int(result[row][2])
                if result[row][3] is None: # in case that the seam doesn't have a score value
                    mark_max = 0
                    seam_ok = True
                else:
                    mark_max = result[row][3]
                    if mark_max < 5: # seams with score equal or more than 5 are bad
                        seam_ok = True
                    else:
                        seam_ok = False
                welding_date = result[row][4][0:19] # extract only the first 19 characters
                voltage_value = result[row][5]
                current_value = result[row][6]
                wire_value = result[row][7]
                gas_value = result[row][8]
                if program_number > 100000: #program number values starts from 100000
                    my_serie = program_number / 100000
                    if my_serie == 1 :
                        mark = "MODEL1"
                    elif my_serie == 2:
                        mark = "MODEL2"
                    elif my_serie == 3:
                        mark = "MODEL3"
                    elif my_serie == 4:
                        mark = "MODEL4"
                    elif my_serie == 5:
                        mark = "MODEL5"
                    elif my_serie == 6:
                        mark = "MODEL6"
                    elif my_serie == 7:
                        mark = "MODEL7"
                    elif my_serie == 8:
                        mark = "MODEL8"
                    elif my_serie == 9:
                        mark = "MODEL9"
                    else:
                        my_serie = -100
                        mark = ""
                    registers[row].set_program(program_number)
                    registers[row].set_mark(mark)
                    registers[row].set_status_ok(seam_ok)
                    registers[row].set_date(welding_date)
                    registers[row].set_voltage(voltage_value)
                    registers[row].set_current(current_value)
                    registers[row].set_wire(gas_value)
                    registers[row].set_wire(wire_value)
                else:
                    msg = "Se encontró un registro con numero de programa invalido"
                    #                                                                   PENDING: ADD MSJ TO GUI!!!!!!
                    logging.error(f"  invalid program_number {program_number}")
            cursor.close()
            conn.close()
            return registers

        else:
            msg = f"""No se encontraron los registros en la pieza con character: {character} por alguno de estos
            motivos:\n
            1.- El programa de esta pieza no esta liberado.\n
            2.- El programa de esta pieza llama a programas de soldadura no existentes.\n
            3.- La base de datos esta vaciá."""
            #                                                                           PENDING: ADD MSJ TO GUI!!!!!!
            logging.error(f"  no result from query")

    except firebirdsql.Error as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"   Unexpected error: {e}")
    finally:
        try:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        except NameError:
            pass


def match_registers(registers: list[Register]) -> list[TrailerHitch]:
    size = len(registers)
    new_serie = registers[size -1].get_serie()
    logging.debug(f"  Starting match_registers with New_serie: {new_serie}  serie: {serie}")
    if serie != -1:
        if new_serie != serie:
            backup_virtual_pieces(serie)
            serie = new_serie
            recover_virtual_pieces(serie)
        else:
            #TBD
    else:
        serie = new_serie
        recover_virtual_pieces(serie)
    processed = process_piece(registers)
    backup_virtual_pieces(serie)
    return processed


def scroll_virtual_pieces():
    pass


def backup_virtual_pieces(serie: int):
    pass


def recover_virtual_pieces(serie: int):
    pass


def run_query(query: str) -> bool:
    pass


def b2int(boo: bool) -> int:
    pass


def query_db(query: str, size: int):
    pass


def get_int_query_mydb(query: str) -> int:
    pass


def set_int_query_mydb(query: str) -> int:
    pass


def get_string_query_mydb(query: str) -> str:
    pass


def store_register_db(register: Register, bmwire: str) -> None:
    #Is not going to be used anymore
    pass


def store_piece_db(piece: str) -> None:
    pass


def set_int_query_extdb(query: str) -> int:
    pass


def save_registers(registers: list[Register], path: str, mode: int) -> None:
    """
    This function stores the seams registers in a CSV file
    :param registers:
    :param path:
    :param mode:
    :return:
    """
    pass


def save_piece(piece: TrailerHitch, path: str) -> None:
    """
    This function stores a piece result data  in a CSV file
    :param piece:
    :param path:
    :return:
    """
    pass


def process_piece(registers: list[Register]) -> TrailerHitch:
    """
    This function inspects all the seams in a piece and return the values in a TrailerHitch class variable
    :param registers:
    :return:
    """
    pass


def in_ranges(val: int, min_a: int, max_a: int, min_b: int, max_b: int) -> bool:
    pass


def cal_b(score) -> bool:
    pass


def cal(score) ->int:
    pass


def restart_execution() -> None:
    pass


def serial_check() -> None:
    pass


def get_db_regdata(index: int) -> str:
    pass


def get_part_number(characters: list[int], series: int, piece_ok: bool, seams_ok: list[int], date: str) -> int:
    pass

if __name__ == '__main__':
    cola = ColaDeque()
