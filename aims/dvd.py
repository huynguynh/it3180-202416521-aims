class DigitalVideoDisc:
    def __init__(self, title: str, category: str = "Unknown", cost: float = 0.0,
                 director: str = "Unknown", length: int = 0):
        self.title = title
        self.category = category
        self.cost = float(cost)
        self.director = director
        self.length = length
