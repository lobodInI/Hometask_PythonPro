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


def view_threads():

    interval_1 = [0, 250000]
    interval_2 = [250001, 500000]
    interval_3 = [500001, 750000]
    interval_4 = [750001, 999999]

    print('>>>>>>>>>>>>>>>>>>>>> START THREADS')

    time_start = time.time()
    test_1 = Thread(target=lucky_recount, args=(interval_1,))
    test_2 = Thread(target=lucky_recount, args=(interval_2,))
    test_3 = Thread(target=lucky_recount, args=(interval_3,))
    test_4 = Thread(target=lucky_recount, args=(interval_4,))
    test_1.start()
    test_2.start()
    test_3.start()
    test_4.start()
    test_1.join()
    test_2.join()
    test_3.join()
    test_4.join()
    time_end = time.time()
    print(f'{"-" * 50}\nЗагальний час пiдрахунку {time_end - time_start} секунди')
    print(f'\n{"*" * 50}')

def view_multiprocess():
    interval_1 = [0, 250000]
    interval_2 = [250001, 500000]
    interval_3 = [500001, 750000]
    interval_4 = [750001, 999999]

    print('>>>>>>>>>>>>>>>>>>>>> START PROCESSES')

    time_start = time.time()
    test_5 = Process(target=lucky_recount, args=(interval_1,))
    test_6 = Process(target=lucky_recount, args=(interval_2,))
    test_7 = Process(target=lucky_recount, args=(interval_3,))
    test_8 = Process(target=lucky_recount, args=(interval_4,))
    test_5.start()
    test_6.start()
    test_7.start()
    test_8.start()
    test_5.join()
    test_6.join()
    test_7.join()
    test_8.join()
    time_end = time.time()
    print(f'{"-" * 50}\nЗагальний час пiдрахунку {time_end - time_start} секунди')
    print(f'\n{"*" * 50}')


if __name__ == '__main__':
    view_threads()
    view_multiprocess()

