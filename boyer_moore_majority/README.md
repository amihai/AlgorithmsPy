# Boyer Moore Majority

Find the majority of a list (sequence of elements) using the Boyer–Moore majority vote algorithm: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm.
The majority element is present in more than half of positions from the sequence of elements.

## Examples of use:

### With numbers:
```
>>> from boyer_moore_majority.boyer_moore_majority import boyer_moore_majority
>>> boyer_moore_majority([1, 2, 3, 1, 4, 1, 1])
1
```

### With strings:
```
>>> boyer_moore_majority(["Trump", "Obama", "Obama", "Trump", "Obama"])
'Obama'
```

### With different types:
```
>>> boyer_moore_majority(["a", "1", "b", "b", -2, "b", "b"])
'b'
```


