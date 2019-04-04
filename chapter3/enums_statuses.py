from enum import Enum, auto


class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    PROCESSED = auto()


class Order:
    def __init__(self):
        self.status = OrderStatus.PENDING

    def process(self):
        if self.status == OrderStatus.PROCESSED:
            raise RuntimeError(
                "Can't process order that has "
                "been already processed"
            )

        self.status = OrderStatus.PROCESSING
        ...
        self.status = OrderStatus.PROCESSED
