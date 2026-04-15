# Finals_LabAct_1
Members:
Misajon, Kynehl Scott
Marabe, Julien
Orencia, Kim
Samuya, Alfred
Sonquipal, Emmanuel

## REFLECTION

### MARABE_Sequential_Searching REFLECTION
In this activity, I implemented a sequential search algorithm and observed how it works by checking each element one by one until the target is found. Sequential execution is simple because it follows a single step-by-step process, while parallel execution divides the task into multiple parts that run at the same time. Because of this, sequential search is easier to implement but may take longer when the dataset becomes large.

During testing, I noticed that the execution time depends on the size of the dataset. With smaller datasets the search finishes quickly, but as the dataset grows, it takes longer because the algorithm may need to check many elements. One challenge during the implementation was making sure the program correctly measures execution time and handles cases where the target is found or not found.

From this activity, I learned that parallel algorithms can potentially improve performance for large datasets, but they also introduce extra overhead such as synchronization and process management. Because of this, sequential algorithms can still be efficient for simpler tasks or smaller datasets.

### Parallel_Sorting_Sonquipal
 I discovered that parallel sorting is more complicated than it appears when I put it into practice. Large datasets can be processed more quickly, but there are additional procedures involved, such as data separation, process management, and result merging. Because of this, it didn’t always perform better, especially for smaller inputs.


## Parallel_Searching_Samuya
In this activity, I learned that parallel searching is a fundamental technique for optimizing data retrieval by breaking down large datasets into smaller, concurrent tasks. By distributing the workload across multiple CPU processes, I was able to see firsthand how performance bottlenecks typical of sequential searches can be mitigated.