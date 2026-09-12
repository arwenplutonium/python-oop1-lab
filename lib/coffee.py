#!/usr/bin/env python3


class Coffee:
    def __init__(self, size, price):
        # size and price are both required from the user
        self.size = size
        self.price = price

    @property
    def size(self):
        # getter returns the stored size
        return self._size

    @size.setter
    def size(self, value):
        # size is only valid if it is Small, Medium, or Large
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # thank the barista and add 1 to the price as a tip
        print("This coffee is great, here's a tip!")
        self.price += 1