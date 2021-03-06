# Boyer Moore Majority

Find the majority of a list (sequence of elements) using the Boyer–Moore majority vote algorithm: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm.  

An element is majority if it is present in more than half of positions from the sequence of elements.

## Examples of use:

### With numbers:
```
>>> from boyer_moore_majority.boyer_moore_majority import boyer_moore_majority
>>> boyer_moore_majority([1, 2, 3, 1, 4, 1, 1])
1
```

### With strings:
```
>>> from boyer_moore_majority.boyer_moore_majority import boyer_moore_majority
>>> boyer_moore_majority(["Trump", "Obama", "Obama", "Trump", "Obama"])
'Obama'
```

### With different types:
```
>>> from boyer_moore_majority.boyer_moore_majority import boyer_moore_majority
>>> boyer_moore_majority(["a", "1", "b", "b", -2, "b", "b"])
'b'
```


