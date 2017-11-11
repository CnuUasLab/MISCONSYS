#===============================================#
#                                               #
#     Singleton implementation for Singleton    #
#     patterns in the Interoperability code.    #
#                                               #
#             Version : 1.0.0                   #
#              Author : David Kroell            #
#                                               #
#      For use by the CNU UAS Team in the       #
#             SUAS AUVSI Competition.           #
#                                               #
#===============================================#

class Singleton:
    """
       Implementation for Singleton pattern for inheritence
       By Singleton classes
    """

    __Instance__ = None

    def __init__(self):
        """ Create singleton instance """