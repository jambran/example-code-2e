import timeit
from itertools import zip_longest, islice

from more_itertools import chunked

l = list(range(10_000))


def batch_iterator(iterable, n):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == n:
            yield batch
            batch = []
    if batch:
        yield batch


def batched(iterable, n):
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch


def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')


if __name__ == '__main__':
    import timeit

    result = timeit.timeit(
        "chunked(l, 5)",
        globals=globals(),
    )
    print(f"chunked result {result}")

    result = timeit.timeit(
        "batch_iterator(l, 5)",
        globals=globals(),
    )
    print(f"Batch iterator result {result}")

    result = timeit.timeit(
        "batched(l, 5)",
        globals=globals(),
    )
    print(f"batched result {result}")

    result = timeit.timeit(
        "grouper(l, 5)",
        globals=globals(),
    )
    print(f"Grouper result {result}")



