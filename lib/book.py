class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.set_page_count(page_count)

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            self._page_count = None
        else:
            self._page_count = value

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
