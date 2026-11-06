from aims.dvd import DigitalVideoDisc
from aims.cart import Cart


def main():
    cart = Cart()
    dvd1 = DigitalVideoDisc("The Lion King", "Animation", 19.95, "Roger Allers", 87)
    dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", 24.95, "George Lucas", 124)
    dvd3 = DigitalVideoDisc("Aladdin", "Animation", 18.99, "John Musker", 90)

    cart.add_dvd(dvd1)
    cart.add_dvd(dvd2)
    cart.add_dvd(dvd3)

    cart.print_cart()
    print(f"Total cost: {cart.total_cost():.2f} $")


if __name__ == "__main__":
    main()
