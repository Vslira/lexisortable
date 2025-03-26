import sys
import unittest
from io import StringIO
from unittest.mock import patch

from lexisortable.cli import main


class TestCLI(unittest.TestCase):
    
    def run_cli(self, args, expected_output=None, expected_error=None, expected_code=0):
        """Helper method to run CLI with given args and test the output."""
        # Override stdin/stdout/stderr
        with patch('sys.argv', ['lexisort'] + args), \
             patch('sys.stdout', new=StringIO()) as fake_out, \
             patch('sys.stderr', new=StringIO()) as fake_err:
            
            # Run the CLI
            exit_code = main()
            
            # Check the output
            if expected_output is not None:
                self.assertEqual(fake_out.getvalue().strip(), expected_output)
                
            # Check the error output
            if expected_error is not None:
                self.assertIn(expected_error, fake_err.getvalue())
                
            # Check the exit code
            self.assertEqual(exit_code, expected_code)
    
    def test_integer_to_lexisort(self):
        self.run_cli(['42'], 'b42')
        self.run_cli(['100'], 'c100')
        
    def test_float_to_lexisort(self):
        self.run_cli(['3.14'], 'a3p14')
        
    def test_lexisort_to_integer(self):
        self.run_cli(['-r', 'b42'], '42')
        
    def test_lexisort_to_float(self):
        self.run_cli(['-r', 'a3p14'], '3.14')
        
    def test_semver_to_lexiver(self):
        self.run_cli(['-v', '1.2.3'], 'a1.a2.a3')
        
    def test_lexiver_to_semver(self):
        self.run_cli(['-rv', 'a1.a2.a3'], '1.2.3')
        
    def test_invalid_input(self):
        self.run_cli(['invalid'], expected_error='Error', expected_code=1)


if __name__ == "__main__":
    unittest.main()