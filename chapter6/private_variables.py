_observers = []


def add_observer(observer):
    _observers.append(observer)


def get_observers():
    """Makes sure _observers cannot be modified."""
    return tuple(_observers)
