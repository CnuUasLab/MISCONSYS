#=====================================#
#                                     #
#	Testing for unittests in all  #
#          Python modules             #
#                                     #
#           Author: David Kroell      #
#          Version: 0.0.1             #
#                                     #
#=====================================#

import sys


sys.path.insert(0, "./Interoperability/src/")
import singleton


def test_singleton():
     assert singleton.test()
