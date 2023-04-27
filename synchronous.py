import time
import logging


logging.basicConfig(level=logging.DEBUG,
                    format="%(processName)s took %(message)s seconds")


def factorize(*numbers):
    numbers_list = []

    for number in numbers:
        numerics_list = []

        for numeric in range(1, number+1):
            if number % numeric == 0:
                numerics_list.append(numeric)
        numbers_list.append(numerics_list)
    return numbers_list


if __name__ == "__main__":
    start = time.time()
    factorize(30093802, 22429787, 40736827, 10651060)
    logging.debug(time.time() - start)



