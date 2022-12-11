"""
Src: Python Algoriothms, Chapter3: Counting 101

Desc:
Show that f(n) is Θ(n) for the implementation of merge sort in Listing 3-2.
"""


def mergesort(seq):
    def _mergesort(seq):
        """T(n) = 2T(n/2) + n"""
        mergesort.calls += 1
        mid = len(seq) // 2
        left, right = seq[:mid], seq[mid:]
        if len(left) > 1: left = _mergesort(left)
        if len(right) > 1: right = _mergesort(right)
        res = []
        while left and right:
            mergesort.fn_calls += 1
            if left[-1] >= right[-1]:
                res.append(left.pop())
            else:
                res.append(right.pop())
        res.reverse()
        mergesort.fn_calls += 1
        return (left or right) + res

    mergesort.calls = 0
    mergesort.fn_calls = 0
    return _mergesort(seq)

if __name__ == '__main__':
    seq = [7, 3, 8, 9, 1, 4, 5, 6]
    output = mergesort(seq)
    print(output)
    print(f"Number of calls: {mergesort.calls}")
    print(f"Number of fn calls: {mergesort.fn_calls}")
