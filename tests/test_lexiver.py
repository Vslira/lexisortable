import unittest

from lexisortable.lexiver import delexiver, lexiver


class TestLexiver(unittest.TestCase):

    def test_lexiver_basic(self):
        # Test basic version numbers
        self.assertEqual(lexiver("1.0.0"), "a1.a0.a0")
        self.assertEqual(lexiver("2.3.4"), "a2.a3.a4")
        self.assertEqual(lexiver("10.20.30"), "b10.b20.b30")
        self.assertEqual(lexiver("0.1.0"), "a0.a1.a0")

    def test_lexiver_ordering(self):
        """Test that version numbers sort correctly with lexicographic sorting."""
        versions = [
            "1.0.0",
            "1.0.1",
            "1.1.0",
            "1.10.0",
            "2.0.0",
            "10.0.0",
            "0.9.9"
        ]

        # Sort the versions semantically
        sorted_versions = sorted(versions, key=lambda v: [int(n) for n in v.split(".")])

        # Convert to lexiversion strings
        lexiversions = [lexiver(v) for v in versions]

        # Sort the strings lexicographically
        sorted_lexiversions = sorted(lexiversions)

        # Convert back to version strings
        result_versions = [delexiver(lv) for lv in sorted_lexiversions]

        # The result should be the same as sorting the original versions semantically
        self.assertEqual(result_versions, sorted_versions)

    def test_delexiver_basic(self):
        # Test basic lexiversions
        self.assertEqual(delexiver("a1.a0.a0"), "1.0.0")
        self.assertEqual(delexiver("a2.a3.a4"), "2.3.4")
        self.assertEqual(delexiver("b10.b20.b30"), "10.20.30")
        self.assertEqual(delexiver("a0.a1.a0"), "0.1.0")

    def test_roundtrip(self):
        # Test that version numbers survive a round trip through lexiver and delexiver
        test_versions = [
            "0.1.0",
            "1.0.0",
            "1.2.3",
            "2.0.0",
            "10.20.30",
            "999.888.777",
        ]

        for v in test_versions:
            self.assertEqual(delexiver(lexiver(v)), v)


if __name__ == "__main__":
    unittest.main()