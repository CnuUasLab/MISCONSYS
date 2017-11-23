import sys

sys.path.insert(0, "./Interoperability/src/")
import singly

def Singleton_Test():
	return singly.test

def test_Interoperability():
	assert Singleton_Test()


