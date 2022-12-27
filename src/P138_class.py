class Counter:
    def __init__(self) -> None:
        self.__count = 0

    def increment(self):
        self.__count += 1

    def get_count(self):
        return self.__count


if __name__ == "__main__":

    # Using int
    counter1 = 0
    print(counter1)

    counter1 += 1
    print(counter1)

    counter1 += 50
    print(counter1)

    counter1 = 8.2
    print(counter1)

    counter1 = -100
    print(counter1)

    # Using Class
    counter2 = Counter()
    print(counter2.get_count())

    counter2.increment()
    print(counter2.get_count())

    counter2.increment()
    counter2.increment()
    counter2.increment()
    print(counter2.get_count())

    counter2.increment()
    # print(counter2.__count)
    print(counter2.get_count())
