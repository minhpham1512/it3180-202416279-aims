from aims import __version__
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart

print(f"AIMS-mini v{__version__}")

cart = Cart()
cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95))
cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 124, 24.95))
cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", "John Musker", 90, 18.99))
cart.print_cart()
