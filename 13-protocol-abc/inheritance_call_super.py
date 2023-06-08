import abc

class Tombola(abc.ABC):  # <1>

    @abc.abstractmethod
    def load(self, iterable):  # <2>
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):  # <3>
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """
        print('inside abstract pick')

    def loaded(self):  # <4>
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())  # <5>

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:  # <6>
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)  # <7>
        return tuple(items)


# end::TOMBOLA_ABC[]


class MyTombola(Tombola):
    def pick(self):
        super(MyTombola, self).pick()
        print("inside MyTombola pick")

    def load(self, iterable):
        pass


if __name__ == '__main__':

    MyTombola().pick()