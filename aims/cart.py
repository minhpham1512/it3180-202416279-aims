MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(d.cost for d in self.items)

    def total_cost_with_discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return self.total_cost() * (100 - percent) / 100

    def print_cart(self):
        print("*********************** CART ***********************")
        if not self.items:
            print("The cart is empty")
        else:
            print("Ordered Items:")
            for i, dvd in enumerate(self.items, start=1):
                print(f"{i}. {dvd}")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("****************************************************")
