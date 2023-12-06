from enum import Enum
from typing import Any


class RecordKey(Enum):
    temperature = 0
    pulse = 1
    blood_pressure = 2
    blood_sugar = 3
    sodium_plasma = 4
    potassium_plasma = 5
    hb = 6
    leucocytes = 7
    thrombocytes = 8
    quick_inr = 9
    aptt = 10

class Record:
    minutes_since_start: float
    value: Any

    def __init__(self, minutes_since_start: float, value: Any):
        self.minutes_since_start = minutes_since_start
        self.value = value

class Visit:
    records: dict[RecordKey, list[Record]]

    def __init__(self, records: dict[RecordKey, list[Record]] = {}):
        self.records = records

    def append(self, key: RecordKey, record: Record):
        if key in self.records:
            self.records[key].append(record)
        else:
            self.records[key] = [record]