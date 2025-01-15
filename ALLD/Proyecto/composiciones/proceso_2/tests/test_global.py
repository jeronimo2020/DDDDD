import pytest
import os
import contextlib

def run_tests():
    result_file = os.path.join(os.path.dirname(__file__), 'test_results_global.txt')
    with open(result_file, 'w') as f:
        with contextlib.redirect_stdout(f):
            pytest.main(['-v', '--tb=short', '--disable-warnings', 'test_unitarios.py', 'test_conjunto.py'])

if __name__ == '__main__':
    run_tests()
