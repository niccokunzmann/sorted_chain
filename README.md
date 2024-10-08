# sorted_chain

`itertools.chain` with sorted result.

This is a simple function. However, it is nice to have it tested and the edge cases taken care of.
If you encounter any problem with this or like to extend it, please open an Issue or Pull Request!

## Installation

You can install `sorted_chain` from PyPI:

```shell
pip install sorted_chain
```

## Usage

You can pass any amount of iterators of sorted values to `sorted_chain()`.
The result will be sorted, then.

```python
>>> from sorted_chain import sorted_chain
>>> list(sorted_chain([1, 3, 5], [2, 4, 6]))
[1, 2, 3, 4, 5, 6]

```

The input iterables must be **sorted**! Otherwise you will receive a `IterableIsNotSorted` exception.

```python
>>> from sorted_chain import IterableIsNotSorted
>>> try:
...     list(sorted_chain([1000, 0]))  # wrong order
... except IterableIsNotSorted:
...     print("error!")
error!

```

Iterators can also be in **decending order**:

```python
>>> list(sorted_chain([100, 10, 1], [99, 9, -1], reverse=True))
[100, 99, 10, 9, 1, -1]

```

The input can be **generators**. Their values are only retrieved when needed.

```python
>>> large_generator1 = iter(range(1000))
>>> large_generator2 = iter(range(1000))
>>> for value in sorted_chain(large_generator1, large_generator2):
...     if value >= 100:
...         break
>>> next(large_generator1)  # this generator had reached 100
101
>>> next(large_generator2)  # this one yielded 99 and 100, too
101

```

If you have elements that you would like to sort with a **key**, you can do that as
expected:

```python
>>> positive = [1, 3, 5]
>>> negative = [-2, -4, -6]
>>> list(sorted_chain(positive, negative, key=lambda x: x*x)) # sort without minus
[1, -2, 3, -4, 5, -6]

```

## Changelog

- v0.0.2

  - Correct metadata
  - Correct license

- v0.0.1

  - Initial release

## New Releases

For a new release:

1. Edit the changelog section
2. Commit the changes
3. Let the GitHub Actions tests run
4. Create a tag and push it:

```shell
git tag v0.0.1
git push origin v0.0.1
```
