#=============================================#
#                                             #
#	Test cases for the python classes     #
#              Author: David Kroell           #
#             Version: 0.0.1                  #
#                                             #
#=============================================#

import sys

# Import interoperability classes for
# unit tests.
sys.path.insert(0, "./Interoperability/src/")
import singly

import pytest

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
