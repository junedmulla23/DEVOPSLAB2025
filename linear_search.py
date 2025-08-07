# linear_search.py
def linear_search(arr, target):
    """Finds the index of a target value in a list. Returns -1 if not found."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i # Target found, return index
    return -1 # Target not found

sample_list = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
search_target = 60

result = linear_search(sample_list, search_target)

if result != -1:
    print(f"Element {search_target} is present at index {result}.")
else:
    print(f"Element {search_target} is not present in the list.")