import time
from multiprocess import Process
from threading import Thread


def lucky_recount(interval):
    count = 0
    for itm in range(interval[0], interval[1]+1):
        num = str(itm).rjust(6, "0")
        if (int(num[0]) + int(num[1]) + int(num[2])) == (int(num[3]) + int(num[4]) + int(num[5])):
            count += 1
    print(f"Кiлькiсть щасливих квиткiв: {count}  |  iнтервал номерiв:  {interval}")


def multithreading(intervals):

    print('>>>>>>>>>>>>>>>>>>>>> START THREADS')

    threads = []
    time_start = time.time()
    for i in intervals:
        th = Thread(target=lucky_recount, args=(i,))
        threads.append(th)

    [x.start() for x in threads]
    [x.join() for x in threads]

    time_end = time.time()
    print(f'{"-" * 50}\nЗагальний час пiдрахунку {time_end - time_start} секунди')
    print(f'\n{"*" * 50}')


def multiprocessing(intervals):

    print('>>>>>>>>>>>>>>>>>>>>> START PROCESSES')

    processes = []
    time_start = time.time()
    for i in intervals:
        pr = Process(target=lucky_recount, args=(i,))
        processes.append(pr)

    [x.start() for x in processes]
    [x.join() for x in processes]

    time_end = time.time()
    print(f'{"-" * 50}\nЗагальний час пiдрахунку {time_end - time_start} секунди')
    print(f'\n{"*" * 50}')


if __name__ == '__main__':

    intervals = [
        [0, 250000],
        [250001, 500000],
        [500001, 750000],
        [750001, 999999]
    ]
    multithreading(intervals)
    multiprocessing(intervals)
