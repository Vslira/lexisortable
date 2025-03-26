#!/usr/bin/env python3
"""
Example usage of the lexisortable package.
"""
from lexisortable import delexisort, lexisort


def main():
    # Generate test numbers (only non-negative)
    integers = [0, 1, 5, 9, 10, 25, 99, 100, 555, 999, 1000, 9999, 10000]
    floats = [0.5, 1.25, 9.99, 10.5, 100.75]

    # All test numbers
    all_numbers = integers + floats

    print("Number -> Lexisortable String\n")
    for number in all_numbers:
        print(f"{number:>10} -> {lexisort(number)}")

    print("\n\nLexicographic vs. Numeric Sorting:\n")

    print("Original numbers:")
    print(all_numbers)

    print("\nNumerically sorted:")
    print(sorted(all_numbers))

    print("\nLexisortable strings:")
    lexisorted = [lexisort(n) for n in all_numbers]
    print(lexisorted)

    print("\nLexicographically sorted:")
    sorted_lexis = sorted(lexisorted)
    print(sorted_lexis)

    print("\nConverted back to numbers:")
    result = [delexisort(s) for s in sorted_lexis]
    print(result)

    # Verify that the result is the same as sorting numerically
    assert result == sorted(all_numbers), "Lexisortable sorting failed!"
    print("\nSuccess! Lexicographic sorting matches numeric sorting.")

    # Demonstrate what happens with negative numbers
    print("\n\nTrying with negative numbers:")
    try:
        print(lexisort(-5))
    except ValueError as e:
        print(f"  Error: {e}")


if __name__ == "__main__":
    main()
