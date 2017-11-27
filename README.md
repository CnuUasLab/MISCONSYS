# MISCONSYS
<b>Mis</b>sion <b>Con</b>trol <b>Sys</b>tem for Ground Station Control

## Current Standing
[![Build Status](https://travis-ci.org/CnuUasLab/MISCONSYS.svg?branch=master)](https://travis-ci.org/CnuUasLab/MISCONSYS)

### Execution
     Put instructions here on how to run the programs, and initiate all of the processes required
     at the time we run the ground station control at the competition.

### Development
In order to start development there are a number of packages that must be installed. For the purposes of integration, python's
testing package must be installed to instantiate tests for all components of the system.
```bash
sudo apt-get install py.test
```
By running ```py.test``` in the root of the repository, the developer will run the test instance for all files.

## Interoperability
The interoperability system on the team is known to interact with the competition server. It uses a hierarchical design, coupled with parrallel processing of different tasks to handle network operations. Using daemons as separate processes, these tasks are given priority in the system. Most of the classes use a singleton design, through a module built, inorder to handle processes that are running simultaneously, and prevent the occurence of two processes working simultaneously. This is accessed as seen in `./Interoperability/src/singly.py`:

```python
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
```

## IMG
