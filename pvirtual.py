
class PVirtual:

    def __init__(self):
        self.status_ok = [False]*5
        self.characters = [-100]*5

    def get_characters(self):
        return self.characters

    def set_characters(self, characters):
        self.characters = characters

    def get_character_val(self, position: int):
        return self.characters[position]

    def set_character_val(self, val: int, position: int):
        self.characters[position] = val

    def get_status_ok(self):
        return self.status_ok

    def set_status_ok(self, status):
        self.status_ok = status

    def get_status_ok_val(self, position : int):
        return self.status_ok[position]

    def set_status_ok_val(self, val : bool, position : int):
        self.status_ok[position] = val