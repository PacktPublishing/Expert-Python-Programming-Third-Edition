class CounterState:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        """Move the counter step towards 0 by 1."""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step


class CountDown:
    def __init__(self, steps):
        self.steps = steps

    def __iter__(self):
        """Return iterable state"""
        return CounterState(self.steps)


if __name__ == "__main__":
    print("Counting down:")

    for element in CountDown(10):
        print('*', element)
        sleep(0.2)
