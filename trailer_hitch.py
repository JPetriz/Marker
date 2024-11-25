WELDING_CELL = "02"

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

    def get_character_val(self, position: int):
        return self.characters[position]

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
        if self.status_ok:
            if self.series == 1:
                marker_text = "MODEL1"
            elif self.series == 2:
                marker_text = "MODEL2"
            elif self.series == 3:
                marker_text = "MODEL3"
            elif self.series == 4:
                marker_text = "MODEL4"
            elif self.series == 5:
                marker_text = "MODEL5"
            elif self.series == 6:
                marker_text = "MODEL6"
            elif self.series == 7:
                marker_text = "MODEL7"
            elif self.series == 8:
                marker_text = "MODEL8"
            elif self.series == 9:
                marker_text = "MODEL9"
            else:
                marker_text = "NoIden"
            marker_text = marker_text + WELDING_CELL
        else:
            marker_text = "REJECTED"
        return  marker_text

    def get_status(self):
        pass


    def get_steps_number(self):
        if self.series == 1:
            result = 3
        elif self.series == 2:
            result = 3
        elif self.series == 3:
            result = 4
        elif self.series == 4:
            result = 4
        elif self.series == 5:
            result = 3
        elif self.series == 6:
            result = 3
        elif self.series == 7:
            result = 3
        elif self.series == 8:
            result = 4
        elif self.series == 9:
            result = 4
        else:
            result = -1
        return result
