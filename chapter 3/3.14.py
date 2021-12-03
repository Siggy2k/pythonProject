# 1
def right_justify(s):
    return " " * (70 - len(s)) + s


def do_twice(method, parameter):
    method(parameter)
    method(parameter)


def printTwice(parameter):
    print(parameter)
    print(parameter)


def do_four(method, parameter):
    do_twice(method, parameter)
    do_twice(method, parameter)


def printLevel(anz):
    printHeader(anz)
    printBetween(anz)
    printBetween(anz)


def printHeader(anz):
    i = 0
    while i < anz:
        print("+", end=" ")

        if i != (anz - 1):
            printValue("-", 4)
        i += 1

    print()


def printBetween(anz):
    i = 0
    while i < anz:
        print("|", end=" ")
        printValue(" ", 4)
        i += 1

    print()


def printValue(value, parm):
    print(value * parm, end=" ")


def printTable22():
    printLevel(3)
    printLevel(3)
    printHeader(3)
    print()


def printTable44():
    printLevel(5)
    printLevel(5)
    printLevel(5)
    printLevel(5)
    printHeader(5)


if __name__ == '__main__':
    print(right_justify("test"))
    do_twice(printTwice, 5);

    printTable22()
    printTable44()
