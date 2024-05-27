# Insertion Sort
Insertion Sort is a straightforward sorting algorithm that builds a sorted array one element at a time by repeatedly picking the next element from the unsorted portion and inserting it into its correct position in the sorted portion.


**Key Points:**

Process:
- Start with the second element.
- Compare it with the elements before it.
- Shift elements that are larger to the right.
- Insert the current element into its correct position.
- Repeat until the entire array is sorted.

**Performance:**
- Best Case: $O(n)$ when the array is already sorted.
- Average and Worst Case: $O(n^2)$ for random or reverse-sorted arrays.
- Space Complexity: $O(1)$ as it sorts in place.

**Characteristics:**
- Stable: Maintains the order of equal elements.
- Adaptive: Efficient for nearly sorted arrays.
- In-Place: Requires no extra memory.

## Example:
For the array [12, 11, 13, 5, 6]:

- Insert 11 before 12 → [11, 12, 13, 5, 6]
- 13 is already in place → [11, 12, 13, 5, 6]
- Insert 5 before 11 → [5, 11, 12, 13, 6]
- Insert 6 after 5 → [5, 6, 11, 12, 13]
