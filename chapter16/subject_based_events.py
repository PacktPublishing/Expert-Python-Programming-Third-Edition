import itertools


class Subject:
    _new_id = itertools.count(1)

    def __init__(self):
        self._id = next(self._new_id)
        self._observers = []

    def register(self, observer):
        self._notify_observers(f"register({observer})")
        self._observers.append(observer)

    def _notify_observers(self, event):
        for observer in self._observers:
            observer.notify(self, event)

    def __str__(self):
        return f"<{self.__class__.__name__}: {self._id}>"


class Observer:
    _new_id = itertools.count(1)

    def __init__(self):
        self._id = next(self._new_id)

    def notify(self, subject, event):
        print(f"{self}: received event '{event}' from {subject}")

    def __str__(self):
        return f"<{self.__class__.__name__}: {self._id}>"

