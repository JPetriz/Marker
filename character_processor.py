import logging, firebirdsql

from cola_deque import ColaDeque
from register import Register
from trailer_hitch import TrailerHitch
from pvirtual import PVirtual

DEBUG = True
level = logging.DEBUG if DEBUG else logging.ERROR
logging.basicConfig(level=level)

HOST = "localhost"
DATABASE = "D:/weldQAS/Data/WELDDB60.GBD"
USER = "SYSDBA"
PASSWORD = "masterkey"

serie_global = -1
virtual_pieces = [PVirtual() for x in range(10)]

def get_registers(character: str) -> list[Register]:
    """
    This function consults the HKS database, search for all the seams with the same character and return them
in a register list object

    :param character: Number or welding process
    :return: List of welding seams
    """
    logging.info(f"   Accessing Data Base")
    try:
        # establish connection to database
        conn = firebirdsql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        # create a cursor
        cursor = conn.cursor()

        # Get the quantity of seams there are with the DESCRIPTION0 = character
        query = (f"SELECT COUNT(DESCRIPTION0) FROM RESULT "
                 f"WHERE (DESCRIPTION0 = '{character}') AND (MARKMAX > 0.0)")

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
            query = (f"SELECT DESCRIPTION0, TECHINDENTNO, MARKMAX, REGISTRATIONDATETIME, MCVALUE1, MCVALUE2, MCVALUE3 "
                     f"FROM RESULT WHERE (DESCRIPTION0 = '{character}') AND (MARKMAX > 0.0) "
                     f"ORDER BY TECHINDENTNO ASC")

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
    logging.debug(f"  Starting match_registers with New_serie: {new_serie}  serie: {serie_global}")
    if serie_global != -1:
        if new_serie != serie_global:
            backup_virtual_pieces(serie_global)
            serie_global = new_serie
            recover_virtual_pieces(serie_global)
        else:
            #TBD
    else:
        serie_global = new_serie
        recover_virtual_pieces(serie_global)

    processed = process_piece(registers)
    backup_virtual_pieces(serie_global)
    return processed


def scroll_virtual_pieces() -> None:
    """
    This function performs a shifting of virtual pieces. (bitwise kind of)
    :return: Nothing
    """
    if (serie_global > 0) and (serie_global < 10) :
        c = 0
        if serie_global == 1:
            c =  3
        elif serie_global == 2:
            c = 3
        elif serie_global == 3:
            c = 4
        elif serie_global == 4:
            c = 4
        elif serie_global == 5:
            c = 5
        elif serie_global == 6:
            c = 6
        elif serie_global == 7:
            c = 7
        elif serie_global == 8:
            c = 8
        elif serie_global == 9:
            c = 9
        c -= 1
        for i in range(c, 0, -1):
            virtual_pieces[c] = virtual_pieces[c-1]
        virtual_pieces[0] = PVirtual()
    else:
        logging.info(f"   A incorrect serie has been detected: {serie_global}")


def backup_virtual_pieces(serie: int) -> None:
    """
    This function stores the virtual pieces in the DB , this function is used when a different model running than the
current one is detected (is detected with the "serie" value)
    :param serie:
    :return: nothing
    """
    pieces_to_backup = 0
    #Key means the index of the data on the Database
    key = -10
    logging.debug(f"  Starting backup_virtual_pieces() with serie: {serie} ")
    if (serie > 0) and (serie < 10) :
        if serie == 1:
            # Registers in MATCH table of Model1 goes from 1 to 3
            key = 1
            pieces_to_backup = 3
        elif serie == 2:
            # Registers in MATCH table of Model2 goes from 4 to 6
            key = 4
            pieces_to_backup = 3
        elif serie == 3:
            # Registers in MATCH table of Model3 goes from 7 to 10
            key = 7
            pieces_to_backup = 3
        elif serie == 4:
            # Registers in MATCH table of Model4 goes from 11 to 14
            key = 11
            pieces_to_backup = 4
        elif serie == 5:
            # Registers in MATCH table of Model5 goes from 15 to 18
            key = 15
            pieces_to_backup = 4
        elif serie == 6:
            # Registers in MATCH table of Model6 goes from 19 to 22
            key = 19
            pieces_to_backup = 4
        elif serie == 7:
            # Registers in MATCH table of Model7 goes from 19 to 22
            key = 19
            pieces_to_backup = 4
        elif serie == 8:
            # Registers in MATCH table of Model8 goes from 23 to 31
            key = 23
            pieces_to_backup = 9
        elif serie == 9:
            # Registers in MATCH table of Model8 goes from 23 to 31
            key = 23
            pieces_to_backup = 9

        query = ["" for i in range(pieces_to_backup)]
        for i in range(pieces_to_backup):
            query[i] = (f"UPDATE MATCH SET "
                        f"PASO_1 = {b2int(virtual_pieces[i].get_status_ok_val(0))}, "
                        f"PASO_2 = {b2int(virtual_pieces[i].get_status_ok_val(1))}, "
                        f"PASO_3 = {b2int(virtual_pieces[i].get_status_ok_val(2))}, "
                        f"PASO_4 = {b2int(virtual_pieces[i].get_status_ok_val(3))}, "
                        f"PASO_5 = {b2int(virtual_pieces[i].get_status_ok_val(4))}, "
                        f"PASO_1_CHARACTER = {virtual_pieces[i].get_character_val(0)}, "
                        f"PASO_2_CHARACTER = {virtual_pieces[i].get_character_val(1)}, "
                        f"PASO_3_CHARACTER = {virtual_pieces[i].get_character_val(2)}, "
                        f"PASO_4_CHARACTER = {virtual_pieces[i].get_character_val(3)}, "
                        f"PASO_5_CHARACTER = {virtual_pieces[i].get_character_val(4)} "
                        f"WHERE \"KEY\" = {key +1};\n")
            logging.debug(f"   Generated query: {query[i]}")
            # Saves virtual piece in the DB
            if run_query(query[i]) is False:
                logging.error("   Virtual piece couldn't be saved in DB")
        logging.debug("   backup_virtual_pieces() has ended")

    else:
        logging.error(f"   A incorrect serie has been detected: {serie}")


def recover_virtual_pieces(serie: int) -> None:
    logging.debug(f"  Starting recover_virtual_pieces() with serie: {serie} ")
    new_serie = serie_global

    # Reassign values to new_serie value because these models uses 2 series for running (SIDE 1 and SIDE 2)
    if (new_serie == 5) or (new_serie == 7):
        new_serie = 6
    if new_serie == 9:
        new_serie = 8

    query = ("SELECT PASO_1, PASO_2, PASO_3, PASO_4, PASO_5, "
             "PASO_1_CHARACTER, PASO_2_CHARACTER, PASO_3_CHARACTER, PASO_4_CHARACTER, PASO_5_CHARACTER, "
             f"\"KEY\" FROM MATCH WHERE SERIE = {new_serie} ORDER BY \"KEY\" ASC;")

    logging.debug(f"  Generated query: {query}")
    result = query_db(query, 11) # the number 11 is fixed
    size = len(result)
    if size >= 0:
        for i in range(size):
            characters = ["","","","",""]
            status_ok = [False, False, False, False, False]
            for j in range(5):
                value = result[i][j]
                if value >= 1:
                    status_ok[j]= True
            for j in range(5, 10):
                characters[j-5] = result[i][j]
            if (i < len(virtual_pieces)):
                virtual_pieces[i].set_status_ok(status_ok)
                virtual_pieces[i].set_characters(characters)
            else
                logging.error("   A surplus virtual piece was recovered and could not be stored")
    else:
        logging.info(f"   0 Registers were found in the DB with the serie = {new_serie}")


def run_query(query: str) -> bool:
    pass


def b2int(boo: bool) -> int:
    pass


def query_db(query: str, size: int): -> list[list[str]]
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
