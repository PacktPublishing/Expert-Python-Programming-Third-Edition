from random import randint


class Container:
    _contents = []

    def append(self, item):
        self._contents.append(item)

    @property
    def unique_items(self):
        return set(self._contents)

    @property
    def ordered_items(self):
        return list(self._contents)


if __name__ == "__main__":
    container = Container()

    for _ in range(20):
        value = randint(0, 10)
        print(f"adding {value}")
        container.append(value)

    print(f"Ordered items: {container.ordered_items}")
    print(f"Unique items:  {container.unique_items}")
