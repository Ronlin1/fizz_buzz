def fizzbuzz(i):
    if i % 15 == 0:
        return "fizzbuzz"
    elif i % 3 == 0:
        return 'fizz'
    elif i % 5 == 0:
        return 'buzz'
    return i


def main():
    for i in range(1, 101):  # pragma: no cover
        print(fizzbuzz(i))


if __name__ == "__main__":  # pragma: no cover
    main()

# An Alternative
"""
num = [i for i in range(1, 101)]

# #print(num)
def fizz_buzz(num_):
    new = []
    for j in range(1, len(num_) + 1):
        if j % 3 == 0 and j % 5 == 0:
            j = 'Fizz - Buzz'
        elif j % 5 == 0:
            j = 'Buzz'
        elif j % 3 == 0:
            j = 'Fizz'
        new.append(j)
    return new
"""