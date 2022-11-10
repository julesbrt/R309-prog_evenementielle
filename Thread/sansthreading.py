import time

if __name__ == '__main__':
    def task(i):
        print(f"Task {i} starts")
        time.sleep(1)
        print(f"Task {i} ends")

    start = time.perf_counter()

    task(1)
    task(2)

    end = time.perf_counter()

    print(f"Tasks ended in {round(end - start, 2)} second(s)")
