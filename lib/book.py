#!/usr/bin/env python3


class Book:
    def __init__(self, title, page_count):
        # title and page_count are both required from the user
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        # getter returns the stored page count
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # page_count must be a whole number
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # simulate the reader flipping to the next page
        print("Flipping the page...wow, you read fast!")