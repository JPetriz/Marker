class Register:

    def __init__(self, date: str = "", character: int = 0, program: int = 0, serie: int = 0, score: float = 0.0, status_ok: bool = False,
                 mark: str = "", voltage: str = "", current: str = "", wire: str = "", gas: str = ""):
        self.date = date
        self.character = character
        self.program = program
        self.serie = serie
        self.score = score
        self.status_ok = status_ok
        self.mark = mark
        self.voltage = voltage
        self.current = current
        self.wire = wire
        self.gas = gas

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_character(self):
        return self.character

    def set_character(self, character):
        self.character = character

    def get_program(self):
        return self.program

    def set_program(self, program):
        self.program = program

    def get_serie(self):
        return self.serie

    def set_serie(self, serie):
        self.serie = serie

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_status_ok(self):
        return self.status_ok

    def set_status_ok(self, status_ok):
        self.status_ok = status_ok

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark

    def get_voltage(self):
        return self.voltage

    def set_voltage(self, voltage):
        self.voltage = voltage

    def get_current(self):
        return self.current

    def set_current(self, current):
        self.current = current

    def get_wire(self):
        return self.wire

    def set_wire(self, wire):
        self.wire = wire

    def get_gas(self):
        return self.gas

    def set_gas(self, gas):
        self.gas = gas

    def compare_to(self):
        pass