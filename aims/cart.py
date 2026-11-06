from aims.dvd import DigitalVideoDisc

MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items: list[DigitalVideoDisc] = []

    def add_dvd(self, dvd: DigitalVideoDisc) -> bool:
        if len(self.items) > MAX_NUMBERS_ORDERED:
            print("The cart is full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def total_cost(self) -> float:
        return round(sum(item.cost for item in self.items), 2)
