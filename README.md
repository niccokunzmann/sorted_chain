# sorted_chain

itertools.chain with sorted result

## Installation

You can install `sorted_chain` from PyPI:

```shell
pip install sorted_chain
```

## Usage

You can sort the iterators:

```python
>>> from sorted_chain import sorted_chain, IterableIsNotSorted
>>> list(sorted_chain([1, 3, 5], [2, 4, 6]))
[1, 2, 3, 4, 5, 6]

```

The input iterables must be sorted! Otherwise you will receive a `IterableIsNotSorted` exception.

```python
>>> from sorted_chain import IterableIsNotSorted
>>> try:
...     list(sorted_chain([1000, 0]))  # wrong order
... except IterableIsNotSorted:
...     print("error!")
error!

```

Iterators can also be in decending order:

```python
>>> list(sorted_chain([100, 10, 1], [99, 9, -1], reverse=True))
[100, 99, 10, 9, 1, -1]

```
