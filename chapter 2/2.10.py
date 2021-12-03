# SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
import math


def exercise211():
    n = 42
    # 42 = n;

    # works
    x = y = 1

    # no need for semicolons

    # doesnt work


def exercise212():
    volume = 4/3*math.pi*5**3
    print (volume);

    price = 24.95 * 60 * 0.6 - (3+59*0.75)
    print (price);

    minutes = 6*60+52;
    neededMinutes = 2*8.15 + 3*7.12;
    time = (minutes+neededMinutes)/60;
    print (time);


if __name__ == '__main__':
    exercise211()
    exercise212()
