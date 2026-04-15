import random
import time
import sys

# 1. CORE LOGIC (Sequential Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    # Sequential execution: one operation at a time [cite: 8]
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 2. DATASET GENERATION [cite: 31, 34]
# Options: 1000 (Small), 100000 (Medium), 1000000 (Large) [cite: 36, 37, 38]
N = 1000 
data = [random.randint(1, 1000000) for _ in range(N)]

# Optional: Test a special case (Already sorted) [cite: 39, 40]
# data.sort() 

# 3. EVALUATION [cite: 70]
print(f"Starting sequential sort for N={N}...")
start = time.time() [cite: 72]

sorted_result = merge_sort(data)

end = time.time() [cite: 74]

# 4. VERIFICATION & RESULTS
print(f"Execution Time: {end - start:.6f} seconds") [cite: 75]
print(f"Is correctly sorted: {sorted_result == sorted(data)}") [cite: 48]
