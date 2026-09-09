class Coffee:
    def __init__(self, size, price):
        self.set_size(size)
        self.price = price

    def get_size(self):
        return self._size

    def set_size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
            self._size = None
        else:
            self._size = value

    size = property(get_size, set_size)

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1

