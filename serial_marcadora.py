from contextlib import nullcontext

import serial, logging, time

DEBUG = True
level = logging.DEBUG if DEBUG else logging.ERROR
logging.basicConfig(level=level, )

RESTART = False

def wait_response(ser: serial, message: str):
    """
    This function reads a Serial Port and keep running until it receives a specific message.

    :param ser: Serial Port
    :param message: Message to wait for
    :return: None
    """
    logging.debug(" Starting Wait_Response")
    response = nullcontext
    try:
        while True: # Do While Simulated
            bytes_count = ser.inWaiting()
            logging.debug(f" bytes count: {bytes_count}")
            if bytes_count == 0:
                logging.debug(" Waiting for message . . . ")
                time.sleep(1)
            else:
                response  = ser.readline().decode().strip()
                logging.debug(f" Received message: {response}")
            if message == response: break   # Ends Do While  Simulated
    except serial.SerialException:
        logging.error(" Error reading Port")
    logging.debug(" Stopping Wait_Response")


def update_list():
    pass


def serial_send():
    """
    10 Carácter de inicio
    02 Dirección de destino de la trama
    xx Longitud total de la trama en HEX
    00 última trama, un solo mensaje
    xx CMD
    XX Datos
    03 Fin de trama sin algoritmo de CRC
    03 Fin de trama sin algoritmo de CRC
    """
    open_file = "\u0010\u0002\u000F\u0000" + "\"" + "MASTER20"+ "\u0003\u0003"
    ack_i_read = "\u0010\u0000\u0007\u0000\u0000\u0003\u0003"
    confirm_i_read = "\u0010\u0000\u0008\u0000\u0032\u0000\u0003\u0003"
    ack_i_send = "\u0010\u0002\u0007\u0000\u0000\u0003\u0003"

    try:
        logging.debug(" Opening serial port COM 5")

        # abrir el puerto serial
        serial_port = serial.Serial('COM5', 9600, 8, "N", 1)

        if serial_port.is_open:
            logging.info(" Serial port opened successfully")
            serial_port.write(open_file.encode())
            wait_response(serial_port, ack_i_read)
            while not RESTART:
                update_list()

    except serial.SerialException:
        print("Error al abrir el puerto serial")
        logging.error(" Failed to open port")

    finally:
        # Asegúrate de cerrar el puerto si está abierto
        if 'ser' in locals() and serial_port.is_open:
            serial_port.close()
            logging.debug(" Serial Port closed successfully")


if __name__ == '__main__':
    logging.debug("  Inicia Serial Marcadora")
