"""
A class which is instantiated only once
"""
import random


class Database:
    initialized = False

    def __init__(self):
        """
        will work smoothly as long as we dont have annything in __init__
        """
        # self.id = random.randint(1,101)
        # print('Generated an id of ', self.id)
        # print('Loading database from file')
        pass

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls) \
                .__new__(cls, *args, **kwargs)

        return cls._instance


database = Database()

if __name__ == '__main__':
    d1 = Database()  # __init__ will be called
    d2 = Database()  # __init__ will be called

    print(d1.id, d2.id)
    print(d1 == d2)
    print(database == d1)
