"""

Do registered subclasses inherit the parent's concrete methods?

"""

from random import randrange


import abc

class MyAbstractClass(abc.ABC):  # <1>

    def concrete_method_in_abstract_class(self):
        print("Concrete method from abstract class")


@MyAbstractClass.register  # <1>
class ConcreteClass:  # <2>

    def make(self):
        print('making!')

    def access_super_class(self):
        return super(ConcreteClass, self)


if __name__ == '__main__':
    cc = ConcreteClass()
    print(cc.make())

    super_class = cc.access_super_class()


    """
    https://docs.python.org/3/library/abc.html
    You can also register unrelated concrete classes (even built-in classes) 
    and unrelated ABCs as “virtual subclasses” – these and their descendants 
    will be considered subclasses of the registering ABC by the built-in 
    issubclass() function, but the registering ABC won’t show up in their 
    MRO (Method Resolution Order) nor will method implementations defined 
    by the registering ABC be callable (not even via super()).
    """
