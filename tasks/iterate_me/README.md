## ITERATE ME (3 POINTS)

`control flow` `list` `range` `enumerate` `reversed` `int` `sum`

### Task

Implement the following functions:

* `get_squares` - returns the square of values. Use `**` for exponentiation
* `get_max_element_index` - returns the index of the maximum element
* `get_every_second_element` - returns a list of second elements
* `get_first_three_index` - returns the index of the first occurrence of three in the list
* `get_last_three_index` - returns the index of the last occurrence of three in the list
* `get_min_max` - returns a `tuple` with a minimum and maximum, if the list is not empty, otherwise the default value for the minimum and maximum. Use `min` and `max`
* `get_by_index` - returns the element by the passed index, if it's greater than the boundary. Otherwise, it returns None. 
Assume that the index always exists. 
Use the `:=` operator and try to write in one line using the ternary operator. See motivation below.

Pay attention to the edge cases. 

### About the Task

Here we practice the selection of the correct iteration. We can iterate:
* by indices
* by values
* by both indices and values
* using for
* using while

Also, using standard structures when you can write without iteration.

Choose the most suitable method for each microtask.

### About `get_by_index`

This is a small model task. Imagine that accessing by index takes quite a long time (some function is calculated inside). The usual code of the type
`return a[i] if a[i] > 0 else 0` takes by index twice. Using the ternary operator will allow you to access by index once and maintain the compactness of the record.

---