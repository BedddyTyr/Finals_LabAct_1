# Finals_LabAct_1
**Members:**<br/> 
Misajon, Kynehl Scott<br/>
Marabe, Julien<br/>
Orencia, Kim<br/>
Samuya, Alfred<br/>
Sonquipal, Emmanuel<br/>

## REFLECTION
### Misajon_generalReflection


### ORENCIA_Sequential_Sorting REFLECTION
The implementation of the sequential Merge Sort algorithm highlights the fundamental nature of linear control flow, where each step must be completed before the next begins. During testing, I observed that the algorithm performed very efficiently on the Small Dataset (1,000 elements), finishing in 0.001928 seconds. As the workload scales to the Medium and Large datasets, I expect the execution time to grow significantly because the performance depends solely on the efficiency of the single-threaded algorithm rather than hardware scaling. This model is straightforward and predictable, with minimal overhead compared to parallel systems.

A primary challenge encountered during implementation was developing the core recursive logic from scratch to ensure the "Divide and Conquer" strategy maintained correctness without built-in functions. Insights gained regarding overhead showed that while sequential execution has no synchronization or communication costs, it is strictly limited by the performance of a single CPU core. Testing verified that parallelism is often unnecessary for small workloads due to the low coordination costs of a sequential approach. However, for larger datasets, parallelism would become beneficial once the computational workload outweighs the coordination and merging overhead required to manage multiple processes.

### MARABE_Sequential_Searching REFLECTION
In this activity, I implemented a sequential search algorithm and observed how it works by checking each element one by one until the target is found. Sequential execution is simple because it follows a single step-by-step process, while parallel execution divides the task into multiple parts that run at the same time. Because of this, sequential search is easier to implement but may take longer when the dataset becomes large.

During testing, I noticed that the execution time depends on the size of the dataset. With smaller datasets the search finishes quickly, but as the dataset grows, it takes longer because the algorithm may need to check many elements. One challenge during the implementation was making sure the program correctly measures execution time and handles cases where the target is found or not found.

From this activity, I learned that parallel algorithms can potentially improve performance for large datasets, but they also introduce extra overhead such as synchronization and process management. Because of this, sequential algorithms can still be efficient for simpler tasks or smaller datasets.

### Parallel_Sorting_Sonquipal
I discovered that parallel sorting is more complicated than it appears when I put it into practice. Large datasets can be processed more quickly, but there are additional procedures involved, such as data separation, process management, and result merging. Because of this, it didn’t always perform better, especially for smaller inputs.


## Parallel_Searching_Samuya
In this activity, I learned that parallel searching is a fundamental technique for optimizing data retrieval by breaking down large datasets into smaller, concurrent tasks. By distributing the workload across multiple CPU processes, I was able to see firsthand how performance bottlenecks typical of sequential searches can be mitigated.