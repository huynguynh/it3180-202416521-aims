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

    def print_cart(self) -> None:
        print("***********************CART***********************")
        if not self.items:
            print("The cart is empty")
        else:
            for idx, dvd in enumerate(self.items, start=1):
                print(
                    f"{idx}. DVD - {dvd.title} - {dvd.category} - "
                    f"{dvd.director} - {dvd.length}: {dvd.cost:.2f} $"
                )
        print(f"Total cost: {self.total_cost():.2f} $")
        print("**************************************************")
