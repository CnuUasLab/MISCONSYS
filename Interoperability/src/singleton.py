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

def Singleton(c):
    """
       Implementation for Singleton pattern for decoration
       By Singleton classes

       c: Class to be implemented as a singleton.
    """

    __Instances__ = {}

    def getInstance():
        """ Static access method for the current instance """
        
        if (c not in __Instances__):
            __Instances__[c] = c()
        return __Instances__[c]
    
    return getInstance
        

#
#  This is for demonstration purposes
#  Just to use as a testing file.
#
@Singleton    # Use decorators for all subsequent classes.
class TestClass():
    def __init__(self):
        self.count = 0
    def inc(self):
        self.count += 1



def test():
    #Instantiate two seperate instances of testclass
    test1 = TestClass()
    test2 = TestClass()

    test1.inc()

    if(not(test1.count == test2.count)):
        return False
    else:
        return True


if __name__ == "__main__":
    result = test()
    print "Singleton class testing: Result: ", result
    
