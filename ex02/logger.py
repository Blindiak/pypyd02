import time
import logging
import getpass
from random import randint

FORMAT = f"({getpass.getuser()})Running: %(message)s"
logging.basicConfig(filename='machine.log', level=logging.DEBUG, format=FORMAT)


def log(func):
    def wrapper(*args, **kwargs):
        try:
            t = time.time()
            lol = func(*args, **kwargs)
            t = time.time() - t
            if t < 1.0:
                t = t * 1000.0
                t = f"{t:.3f} ms"
            else:
                t = f"{t:.3f} s "
            logging.info("%-15s [ exec-time =  %s ]" % (func.__name__.replace(
                "_", " ").title(
            ), t))
            return lol
        except Exception as e:
            logging.fatal(e)
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
