from multiprocessing import Process, Queue
import time
import random

def search_chunk(chunk, target, queue, start_index):
    for i in range(len(chunk)):
        if chunk[i] == target:
            queue.put(start_index + i)
            return
    queue.put(-1)


def parallel_search(data, target, num_processes=4):
    processes = []
    result_queue = Queue()
    size = len(data)
    chunk_size = size // num_processes

    for i in range(num_processes):
        start = i * chunk_size
        end = size if i == num_processes - 1 else (i + 1) * chunk_size

        chunk = data[start:end]
        p = Process(target=search_chunk, args=(chunk, target, result_queue, start))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = [result_queue.get() for _ in processes]

    for res in results:
        if res != -1:
            return res

    return -1


if __name__ == "__main__":
    data = [random.randint(1, 1000000) for _ in range(100000)]
    target = data[50000]

    start_time = time.perf_counter()

    index = parallel_search(data, target)

    end_time = time.perf_counter()

    if index != -1:
        print(f"Target found at index: {index}")
    else:
        print("Target not found")

    print(f"Time taken: {end_time - start_time:.6f} seconds")