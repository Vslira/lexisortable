import unittest

from lexisortable import delexisort, lexisort


class TestLexisortable(unittest.TestCase):

    def test_integers(self):
        # Test single digit numbers
        self.assertEqual(lexisort(0), "a0")
        self.assertEqual(lexisort(5), "a5")
        self.assertEqual(lexisort(9), "a9")

        # Test double digit numbers
        self.assertEqual(lexisort(10), "b10")
        self.assertEqual(lexisort(42), "b42")
        self.assertEqual(lexisort(99), "b99")

        # Test triple digit numbers
        self.assertEqual(lexisort(100), "c100")
        self.assertEqual(lexisort(555), "c555")
        self.assertEqual(lexisort(999), "c999")

        # Test some larger numbers
        self.assertEqual(lexisort(1000), "d1000")
        self.assertEqual(lexisort(10000), "e10000")
        self.assertEqual(lexisort(100000), "f100000")

    def test_negative_integers_raises_error(self):
        # Test that negative numbers raise ValueError
        with self.assertRaises(ValueError):
            lexisort(-1)

        with self.assertRaises(ValueError):
            lexisort(-10)

        with self.assertRaises(ValueError):
            lexisort(-100)

    def test_mole_limit_raises_error(self):
        # Test that numbers larger than a mole raise ValueError
        from math import pow

        from lexisortable.lexisortable import LOG10_MOLE_2019

        # Just below the limit should work
        mole_minus = pow(10, LOG10_MOLE_2019 - 0.000001)
        lexisort(mole_minus)  # Should not raise

        # At the limit or above should raise ValueError
        mole = pow(10, LOG10_MOLE_2019)
        with self.assertRaises(ValueError):
            lexisort(mole)

        mole_plus = pow(10, LOG10_MOLE_2019 + 0.000001)
        with self.assertRaises(ValueError):
            lexisort(mole_plus)

    def test_floats(self):
        # Test positive floats
        self.assertEqual(lexisort(1.5), "a1p5")
        self.assertEqual(lexisort(3.14), "a3p14")
        self.assertEqual(lexisort(10.25), "b10p25")
        self.assertEqual(lexisort(100.75), "c100p75")

        # Test floats with trailing zeros
        self.assertEqual(lexisort(1.50), "a1p5")
        self.assertEqual(lexisort(10.10), "b10p1")

        # Test negative floats raise ValueError
        with self.assertRaises(ValueError):
            lexisort(-1.5)

        with self.assertRaises(ValueError):
            lexisort(-3.14)

        # Test floats that are actually integers
        self.assertEqual(lexisort(1.0), "a1")
        self.assertEqual(lexisort(10.0), "b10")

    def test_lexicographic_order(self):
        """Test that numbers sort correctly with lexicographic sorting."""
        numbers = [0, 0.5, 1, 5, 9, 10, 42, 100, 0.1, 0.9, 1.1, 1.9, 9.1, 9.9, 10.1]

        # Sort the numbers
        sorted_numbers = sorted(numbers)

        # Convert to lexisortable strings
        lexicographically_sortable = [lexisort(n) for n in numbers]

        # Sort the strings lexicographically
        sorted_strings = sorted(lexicographically_sortable)

        # Convert back to numbers
        result_numbers = [delexisort(s) for s in sorted_strings]

        # The result should be the same as sorting the original numbers
        self.assertEqual(result_numbers, sorted_numbers)

    def test_delexisort(self):
        # Test integers
        self.assertEqual(delexisort("a0"), 0)
        self.assertEqual(delexisort("a5"), 5)
        self.assertEqual(delexisort("b10"), 10)
        self.assertEqual(delexisort("c100"), 100)

        # Test floats
        self.assertEqual(delexisort("a1p5"), 1.5)
        self.assertEqual(delexisort("a3p14"), 3.14)

    def test_roundtrip(self):
        # Test that numbers survive a round trip through lexisort and delexisort
        test_numbers = [
            0,
            1,
            9,
            10,
            42,
            99,
            100,
            555,
            999,
            1000,
            10000,
            0.1,
            1.5,
            3.14,
            10.25,
            100.75,
        ]

        for n in test_numbers:
            self.assertEqual(delexisort(lexisort(n)), n)


if __name__ == "__main__":
    unittest.main()
