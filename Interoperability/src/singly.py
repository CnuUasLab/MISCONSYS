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
        """ 
        Create singleton instance or use instance already created.
        This is a virtually private constructor.
        DO NOT CALL THIS - Call getInstance() when accessing
        singleton class.
        """
        if (Singleton.__Instance__ == None):
            Singleton.__Instance__ = self
        else:
            raise Exception("singleton instance defined.")

    @staticmethod
    def getInstance():
        """ Static access method for the current instance """
        if(Singleton.__Instance__ == None):
            Singleton()

        return Singleton.__Instance__

