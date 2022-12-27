from P138_class import Counter


class CounterUpgrade(Counter):
    def increment_group(self, count=5):
        self._count += count


if __name__ == "__main__":
    counter3 = CounterUpgrade()
    print(counter3.get_count())

    counter3.increment()
    print(counter3.get_count())

    counter3.increment_group()
    print(counter3.get_count())
