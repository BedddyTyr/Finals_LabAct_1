import random
import time
# duha lagi ni part? 

def sequential_search(data, target):
    """
    Searches for the target value one-by-one.
    Returns the index if found, otherwise -1.
    """
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


if __name__ == "__main__":
    # Generate dataset
    data = [random.randint(1, 1000000) for _ in range(100000)]
    target = data[50000]  # guaranteed to exist

    # Measure execution time
    start = time.time()
    index = sequential_search(data, target)
    end = time.time()

    # Output result
    if index != -1:
        print(f"Target found at index: {index}")
    else:
        print("Target not found")

    print(f"Execution Time: {end - start:.6f} seconds")