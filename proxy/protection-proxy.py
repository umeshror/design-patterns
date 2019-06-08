"""

An interface for accessing a particular resource

A proxy is a class which functions as an interface to a particular resource and that

resource can be remote it can be expensive to construct or it may require logging or some other added

functionality and the way that the proxy adds it is such that your interface is typically unchanged.

"""
class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car being driven by {self.driver.name}')

class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self.car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self.car.drive()
        else:
            print('Driver too young')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    car = CarProxy(Driver('John', 12))
    car.drive()