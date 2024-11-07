from matplotlib import pyplot as plt
from numpy import linspace
from random import randint

def plot_function(f, a, b):
    xs = linspace(a,b,257)
    ys = f(xs)
    plt.plot(xs, ys)
    plt.show()

class Chooser:
    def __init__(self, list):
        self.list = list
    def choose(self):
        return self.list[randint(0, len(self.list)-1)]
    
def largest_prime_factor(n):
    f = 2
    while f*f <= n:
        if n%f == 0:
            n = n//f
        else:
            f += 1
    return n

def fast_flip_num(n):
    m = 0
    while n != 0:
        m *= 10
        n, d = divmod(n, 10)
        m += d
    return m

if __name__ == '__main__':
    print('Test plot:')
    plot_function(lambda x: x*x, -1, 1)
    greeting = Chooser(['Hi!', 'Hello.', 'How are you?'])
    print('Test greeting:', greeting.choose())
    print('Test factor:', largest_prime_factor(600851475143))
    print('Test flip:', fast_flip_num(123))