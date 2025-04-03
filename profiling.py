from multiprocessing import Process

import time
from psycopg_db import DbInterface

if __name__ == '__main__':
    db_interface = DbInterface()
    batch_size = 1000

    # write a general multiprocessing func in order to test 2 workers/conns, 5 workers/cons, 50 w/c
    # increase test batch size to 5000

    def make_workers(n):
        p_list = []
        for i in range(n):
            p = Process(target=db_interface.loop_over_tasks(number_of_tasks=int(batch_size/n)))
            p_list.append(p)
        return p_list

    def test_n_workers(n):
        t1 = time.perf_counter(), time.process_time()

        workers_list = make_workers(n)
        for w in workers_list:
            w.start()

        for w in workers_list:
            w.join()

        t2 = time.perf_counter(), time.process_time()

        print(f"{n} workers multiprocessing person real time: {t2[0] - t1[0]:.2f} seconds")
        print(f"{n} workers multiprocessing person CPU time: {t2[1] - t1[1]:.2f} seconds")

    test_n_workers(2)
    test_n_workers(5)
    test_n_workers(50)

    t1 = time.perf_counter(), time.process_time()
    for i in range(batch_size):
        db_interface.get_one_person()

    t2 = time.perf_counter(), time.process_time()

    print(f"one person real time: {t2[0] - t1[0]:.2f} seconds")
    print(f"one person CPU time: {t2[1] - t1[1]:.2f} seconds")

    t1 = time.perf_counter(), time.process_time()

    db_interface.get_multiple_persons(batch_size)

    t2 = time.perf_counter(), time.process_time()

    print(f"{batch_size} persons real time: {t2[0] - t1[0]:.2f} seconds")
    print(f"{batch_size} persons CPU time: {t2[1] - t1[1]:.2f} seconds")
    db_interface.close_pool()