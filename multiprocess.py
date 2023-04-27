import time
from multiprocessing import Process
import logging


logging.basicConfig(level=logging.DEBUG,
                    format="%(processName)s %(message)s")


def factorize(number):
    start = time.time()
    logging.debug(f"start at {time.ctime(start)}")
    numerics_list = []

    for numeric in range(1, number+1):
        if number % numeric == 0:
            numerics_list.append(numeric)
    logging.debug(f"took {time.time() - start}")
    return numerics_list


if __name__ == "__main__":
    start = time.time()
    numbers = [30093802, 22429787, 40736827, 10651060]
    processes_list = []

    for number in numbers:
        pr = Process(target=factorize, args=(number, ))
        pr.start()
        processes_list.append(pr)

    [el.join() for el in processes_list]
    
    logging.debug(f"took {time.time() - start}")

