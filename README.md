# lexisortable

A Python library for converting non-negative integers and floats into lexicographically sortable string representations. This allows for natural string sorting of numbers.

## Installation

```bash
pip install lexisortable
```

## Usage

```python
from lexisortable import lexisort, delexisort

# Converting integers to sortable strings
print(lexisort(0))   # 'a0'
print(lexisort(9))   # 'a9'
print(lexisort(10))  # 'b10'
print(lexisort(100)) # 'c100'

# Converting floats
print(lexisort(3.14))  # 'a3p14'
print(lexisort(10.5))  # 'b10p5'

# Converting back to original numbers
print(delexisort('a0'))     # 0
print(delexisort('c100'))   # 100
print(delexisort('a3p14'))  # 3.14

# Attempting to use negative numbers raises an error
try:
    lexisort(-5)  # ValueError: lexisort only accepts non-negative numbers (>= 0)
except ValueError as e:
    print(e)
```

## How It Works

The library converts numbers to strings with a prefix character that corresponds to the number of digits:

```
a0, a1, ..., a9       (single digit)
b10, b11, ..., b99     (double digits)
c100, c101, ..., c999  (triple digits)
...
z[max digits]9         (26 digits)
za[max+1 digits]0      (27 digits)
...
```

Floats replace the decimal point with 'p' to maintain lexicographic ordering.

## Limitations

- Upper bound of one [mole (2019 SI revision)](https://en.wikipedia.org/wiki/Mole_(unit)) on sortable values
- Only works with non-negative numbers (0 and above)
    - Attempting to use negative numbers will raise a ValueError

## License

See the [LICENSE](LICENSE) file for details.
