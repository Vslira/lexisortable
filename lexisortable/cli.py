#!/usr/bin/env python3
import argparse
import sys

from lexisortable import delexisort, delexiver, lexisort, lexiver


def main():
    parser = argparse.ArgumentParser(
        description="Convert between numbers/versions and their lexicographically sortable representations."
    )
    parser.add_argument(
        "input", 
        help="The number or version string to convert"
    )
    parser.add_argument(
        "-v", "--version", 
        action="store_true", 
        help="Treat input as semver and convert to/from lexiver format"
    )
    parser.add_argument(
        "-r", "--reverse", 
        action="store_true", 
        help="Reverse the conversion (convert from lexisortable to original format)"
    )

    args = parser.parse_args()

    try:
        if args.version:
            # Handle semantic version
            if args.reverse:
                # Convert from lexiver to semver
                result = delexiver(args.input)
            else:
                # Convert from semver to lexiver
                result = lexiver(args.input)
        else:
            # Handle number
            if args.reverse:
                # Convert from lexisort to number
                result = delexisort(args.input)
            else:
                # Convert from number to lexisort
                try:
                    # Try as integer first
                    value = int(args.input)
                except ValueError:
                    # If not an integer, try as float
                    value = float(args.input)
                result = lexisort(value)

        print(result)
        return 0
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())