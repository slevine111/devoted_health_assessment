from typing import Dict


class DatabaseConstructor:
    def __init__(self, data: Dict[str, str] = None, count_by_value: Dict[str, int] = None):
        self.data: Dict[str, str] = data or {}
        self.count_by_value: Dict[str, int] = count_by_value or {}

    def set(self, name: str, value: str):
        if self.data.get(name):
            value_decrement = self.data[name]
            self.count_by_value[value_decrement] = self.count_by_value[value_decrement] - 1
            if self.count_by_value[value_decrement] == 0:
                del self.count_by_value[value_decrement]
        self.data[name] = value
        self.count_by_value[value] = self.count_by_value.get(value, 0) + 1

    def get(self, name: str):
        print(self.data.get(name, 'NULL'))

    def delete(self, name: str):
        if self.data.get(name):
            value = self.data[name]
            self.count_by_value[value] = self.count_by_value[value] - 1
            if self.count_by_value[value] == 0:
                del self.count_by_value[value]
            del self.data[name]

    def count(self, value: str):
        print(self.count_by_value.get(value, 0))
