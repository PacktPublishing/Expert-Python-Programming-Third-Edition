class Base(object):
    def __secret(self):
        print("don't tell")

    def public(self):
        self.__secret()


class Derived(Base):
    def __secret(self):
        print("never ever")


if __name__ == "__main__":

    print("Base class members:", dir(Base))
    print("Derived class members:", dir(Derived))

    print("Base.public() result:")
    Base().public()

    print("Derived.public() result:")
    Derived().public()
