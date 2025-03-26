# lexisortable

A Python library for converting non-negative integers and floats into lexicographically sortable string representations. This allows for natural string sorting of numbers.

## Installation

This project is ~~AI slop~~ vibe coded, so out of respect I didn't add it to PyPI.
Install it directly with pip - or vendor it in, it's just a couple of files and a lot safer:

```bash
pip install git+https://github.com/Vslira/lexisortable.git
```

## Usage

### Python API

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

### Version Handling

```python
from lexisortable import lexiver, delexiver

# Converting semantic versions to sortable strings
print(lexiver("1.0.0"))    # 'a1.a0.a0'
print(lexiver("2.10.5"))   # 'a2.b10.a5'

# Converting back to semantic versions
print(delexiver("a1.a0.a0"))    # '1.0.0'
print(delexiver("a2.b10.a5"))   # '2.10.5'
```

### Command Line Interface

The package includes a command-line interface for quick conversions:

```bash
# Convert a number to lexisortable format
$ lexisortable 42
b42

# Convert a lexisortable string back to a number
$ lexisortable -r b42
42

# Convert a semantic version to lexiver format
$ lexisortable -v 2.10.5
a2.b10.a5

# Convert a lexiver string back to a semantic version
$ lexisortable -v -r a2.b10.a5
2.10.5
```

## How It Works

The library converts numbers to strings with a prefix character that corresponds to the number of digits:

```
a0, a1, ..., a9       (single digit)
b10, b11, ..., b99     (double digits)
c100, c101, ..., c999  (triple digits)
...
```

Floats replace the decimal point with 'p' to maintain lexicographic ordering.

## Limitations

- Upper bound of one [mole (2019 SI revision)](https://en.wikipedia.org/wiki/Mole_(unit)) on sortable values
- Only works with non-negative numbers (0 and above)
    - Attempting to use negative numbers will raise a ValueError

## License

See the [LICENSE](LICENSE) file for details.
