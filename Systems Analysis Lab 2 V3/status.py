from enum import Enum

class Status(Enum):
    FORSALE = 1
    UNDEROFFER = 2
    SALEAGREED = 3
    SOLD = 4
    WITHDRAW = 5