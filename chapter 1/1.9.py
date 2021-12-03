# 1 SyntaxError: '(' was never closed
# 2 SyntaxError: unterminated string literal
# 3 works as expected
# 4 Python version 3.10 does not support this syntax. It requires '0o' prefix for octal literals
# 5 the program cant determine that it should be 2 values

# 1
def exercise121():
    value = 42 * 60 + 42;
    return 42 * 60 + 42;


# 2
def exercise122():
    value = 10 / 1.61;
    return value;


# 3
def exercise123():
    seconds = exercise121();
    miles = exercise122();

    milePerSecond = miles / seconds;
    print (milePerSecond);

    milePerHour = milePerSecond * 60 * 60;
    print (milePerHour);


if __name__ == '__main__':
    print (exercise121());
    print (exercise122());
    exercise123();
