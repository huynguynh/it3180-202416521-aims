from aims.dvd import DigitalVideoDisc


def search_by_title(
    items: list[DigitalVideoDisc], keyword: str
) -> list[DigitalVideoDisc]:
    return [dvd for dvd in items if keyword in dvd.title]
