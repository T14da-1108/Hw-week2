## REVERSE LIST (3 POINTS)

`control flow` `iteration` `list` `len` `job interview` `reversed` `slicing` `unpacking`

### Task

Write 5 functions. 

**1.** `reverse_iterative` - takes a list and **returns a new** list where the elements are in reverse order

* **Use iteration only**
* Don't change the input lists inside the function. We will discuss why it affects and why not to do so in the next lecture
* Estimate the time and memory complexity - it should be O(n) in speed and O(n) in memory ([Big O Notation](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/))


**2.** `reverse_inplace_iterative` - **updates** the passed list so that the elements are in reverse order

* **Use iteration only**
* Note that you don't need to go through the entire list for this
* Estimate the time and memory complexity - it should be O(n) in speed and O(1) in memory
* How to do it? Google "reverse list inplace algorithm"

**3.** `reverse_inplace` - **updates** the passed list so that the elements are in reverse order

* **Use only the [`reverse()`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) method of the list**

**4.** `reverse_reversed` - takes a list and **returns a new** list where the elements are in reverse order

* **Use the `reversed` function**
* Note that you need to convert the result of `reversed` to `list`

**5.** `reverse_slice` - takes a list and **returns a new** list where the elements are in reverse order

* **Use slices**


### About the Task

This task is probably the first thing that comes to mind when mentioning screening sections.

The last three implementations are the `pythonic way` for the same task.

---