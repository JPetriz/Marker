class TrailerHitch:
    """

    """

    def __init__(self, characters: list[int], part_number: int, series: int, status_ok: bool, date: str):
        self.characters = characters
        self.part_number = part_number
        self.series = series
        self.status_ok = status_ok
        self.date = date

    def get_characters(self):
        return self.characters

    def set_characters(self, characters: list[int]):
        self.characters = characters

    def set_character_val (self, value: int, position: int):
        self.characters[position] = value

    def get_part_number(self):
        return self.part_number

    def set_part_number(self, part_number: int):
        self.part_number = part_number

    def get_series(self):
        return self.series

    def set_series(self, series: int):
        self.series = series

    def get_status_ok(self):
        return self.status_ok

    def set_status_ok(self, status_ok: bool):
        self.status_ok = status_ok

    def get_date(self):
        return self.date

    def set_date(self, date: str):
        self.date = date

    def get_model(self):
        model = []
        return  model

    def get_status(self):
        pass

