def boyer_moore_majority(elements):
    """
    Find the majority of a list (sequence of elements) using the Boyer–Moore majority vote algorithm: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm.
    The majority element is present in more than half of positions from the sequence of elements.
    """
    if len(elements) == 0:
        return None

    candidate = None
    candidate_counter = 0

    for element in elements:
        if candidate_counter == 0:
            candidate = element
            candidate_counter = 1
        elif candidate == element:
            candidate_counter = candidate_counter + 1
        else:
            candidate_counter = candidate_counter - 1

    # Verify the candidate
    if elements.count(candidate) > len(elements) / 2:
        return candidate
    else:
        return None # No majority


# --------------------------------------
# Test the boyer_moore_majority function
# --------------------------------------
if __name__ == '__main__':
    # Happy Flow - odd number of elements
    assert boyer_moore_majority([3, 1, 2, 1, 1]) == 1

    # Happy Flow - even number of elements
    assert boyer_moore_majority([3, 1, 1, 1]) == 1

    # Happy Flow - sorted asc array
    assert boyer_moore_majority([1, 2, 3, 4, 4, 4, 4]) == 4

    # Happy flow - strings
    assert boyer_moore_majority(["Trump", "Obama", "Obama", "Trump", "Obama"]) == "Obama"

    # Happy Flow - sorted desc array
    assert boyer_moore_majority([7, 6, 5, 4, 3, 3, 3, 3, 3]) == 3

    # Empty List
    assert boyer_moore_majority([]) is None

    # No majority - even array length
    assert boyer_moore_majority([3, 1, 2, 4]) is None

    # No majority - odd array length
    assert boyer_moore_majority([3, 1, 2, 4, -6]) is None

    # No majority - only one element is missing to be a majority
    assert boyer_moore_majority([1, 1, 1, 2, 2, 2]) is None

    print("All tests were passed.")
