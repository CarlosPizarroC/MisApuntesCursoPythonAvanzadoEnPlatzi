### Se crea un iterador que extrae los elementos de la sucesión de Fibonacci hasta un número máximo

from time import sleep
class FibonacciIter:

    def __init__(self, max: int=None):
        self.max: int = max

    def __iter__(self):
        self.n1: int = 0
        self.n2: int = 1
        self.counter: int = 0
        return self

    def __next__(self):
        while True:
            if self.counter == 0:
                print(0)
                self.counter += 1
            elif self.counter == 1:
                print(1)
                self.counter += 1
            else:
                self.aux: int
                self.aux = self.n1 + self.n2
                if (not self.max) or (self.aux <= self.max):
                    self.n1, self.n2 = self.n2, self.aux
                    self.counter += 1
                    return self.aux
                else:
                    raise StopIteration



def run():
    fibonacci = FibonacciIter(1000)
    for element in fibonacci:
        sleep(0.05)
        print(element)


if __name__ == '__main__':
    run()