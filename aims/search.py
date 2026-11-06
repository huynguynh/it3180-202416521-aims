from aims.dvd import DigitalVideoDisc


def search_by_category(
    items: list[DigitalVideoDisc], category: str
) -> list[DigitalVideoDisc]:
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]


def search_by_title(
    items: list[DigitalVideoDisc], keyword: str
) -> list[DigitalVideoDisc]:
    return [dvd for dvd in items if keyword in dvd.title]
