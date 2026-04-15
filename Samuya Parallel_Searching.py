from multiprocessing import Process, Queue

def search_chunk(chunk, target, queue, start_index):
    """
    Searches for the target inside a chunk of data.
    If found, returns the global index using the queue.
    """
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

    # Create processes
    for i in range(num_processes):
        start = i * chunk_size
        end = size if i == num_processes - 1 else (i + 1) * chunk_size

        chunk = data[start:end]
        p = Process(target=search_chunk, args=(chunk, target, result_queue, start))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    # Collect results
    results = [result_queue.get() for _ in processes]

    # Return the first valid index found
    for res in results:
        if res != -1:
            return res

    return -1


# Example usage
if _name_ == "_main_":
    import random

    data = [random.randint(1, 1000000) for _ in range(100000)]
    target = data[50000]  # pick a value that exists

    index = parallel_search(data, target)

    if index != -1:
        print(f"Target found at index: {index}")
    else:
        print("Target not found")